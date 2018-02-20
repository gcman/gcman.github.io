from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver
from datetime import datetime
import livereload
import webbrowser
import markdown2
from itertools import chain
from glob import iglob
from shutil import copyfile
from git import Repo
from pelican.server import ComplexHTTPRequestHandler

ROOT = os.getcwd()

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
PORT = 8000
TEMPLATE = """
---
title: {title}
date: {day} {month} {year}
category:
tags:
slug: {slug}
status: draft
---


"""
repo = Repo(os.path.dirname(__file__))
assert not repo.bare
diff = [os.path.basename(x) for x in [item.a_path for item in repo.index.diff(None)]]

def remove_prefix(text, prefix):
	if text.startswith(prefix):
		return text[len(prefix):]
	return text

def clean():
	"""Remove generated files"""
	if os.path.isdir(DEPLOY_PATH):
		keep = ["pdf","raw","figures"]
		for file in [x for x in os.walk(DEPLOY_PATH)][0][2]:
			os.remove(os.path.join(DEPLOY_PATH,file))
		for dir in [x for x in os.walk(DEPLOY_PATH)][0][1]:
			if dir not in keep:
				shutil.rmtree(os.path.join(DEPLOY_PATH,dir))
		os.makedirs(DEPLOY_PATH,exist_ok=True)

def build():
	"""Build local version of site"""
	local('pelican -s pelicanconf.py')

def rebuild():
	"""`build` with the delete switch"""
	local('pelican -d -s pelicanconf.py')

def regenerate():
	"""Automatically regenerate site upon file modification"""
	local('pelican -r -s pelicanconf.py')

def serve():
	"""Serve site at http://localhost:8000/"""
	os.chdir(env.deploy_path)

	class AddressReuseTCPServer(socketserver.TCPServer):
		allow_reuse_address = True

	server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

	sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
	server.serve_forever()

def reserve():
	"""`build`, then `serve`"""
	build()
	serve()

def preview():
	"""Build production version of site"""
	local('pelican -s publishconf.py')

@hosts(production)

def post(title):
	today = datetime.today()
	slug = title.lower().strip().replace(' ', '-')
	f_create = "content/{}_{:0>2}_{:0>2}_{}.md".format(
		today.year, today.month, today.day, slug)
	t = TEMPLATE.strip().format(title=title,
								year=today.strftime("%Y"),
								month=today.strftime("%B"),
								day=today.strftime("%d").lstrip("0"),
								slug=slug)
	with open(f_create, 'w') as w:
		w.write(t)
	print("File created -> " + f_create)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		make_entry(sys.argv[1])
	else:
		print("No title given")

def live(port=8080):
	clean()
	rebuild()
	os.chdir('output')
	server = livereload.Server()  # 4
	webbrowser.open("http://127.0.0.1:8080")
	server.watch('../content/*.md',  # 5
		livereload.shell('pelican -s ../pelicanconf.py -o ../output'))  # 6
	server.watch('../pelican-themes/cebong/',  # 7
		livereload.shell('pelican -s ../pelicanconf.py -o ../output'))  # 8
	server.watch('*.html')  # 9
	server.watch('*.css')  # 10
	server.serve(liveport=35729, port=port)  # 11

def make_figs():
	os.chdir('content/figures')
	rootdir = os.getcwd()
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			ext = os.path.splitext(file)[-1].lower()
			if ext == ".tex":
				if file in diff or not os.path.isfile(os.path.join(rootdir,os.path.splitext(file)[0]+".pdf")):
					local("latexmk " + file + " -pdf -quiet")
					local("latexmk -c")
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			ext = os.path.splitext(file)[-1].lower()
			if ext == ".pdf":
				if file in diff or not os.path.isfile(os.path.join(rootdir,os.path.splitext(file)[0]+".png")):
					local("magick -density 400 -background none -antialias " + file + " -quality 1000 -trim " + file.strip(".pdf") + ".png")
	os.chdir(ROOT)

def make_source():
	os.chdir('content')
	rootdir = os.getcwd()
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			ext = os.path.splitext(file)[-1].lower()
			if ext == ".md":
				with open(file, "r") as f:
					data = markdown2.markdown(f.read(), extras=["metadata"]).metadata
					slug = data["slug"].lower()
					out = os.path.join(os.path.dirname(os.getcwd()),"output")
					rawdir = os.path.join(out,"raw")
					pdfdir = os.path.join(out,"pdf")
					os.makedirs(rawdir,exist_ok=True)
					os.makedirs(pdfdir,exist_ok=True)
					if file in diff or not os.path.isfile(os.path.join(rawdir,slug+".md")):
						copyfile(file,os.path.join(rawdir,slug+".md"))
					if file in diff or os.path.join(ROOT, "/content/extra/header.tex") in diff or not os.path.isfile(os.path.join(pdfdir,slug+".pdf")):
						local("pandoc extra/default.yaml -H extra/header.tex --template extra/template.tex --listings "
							+ file + " -o " + "../output/pdf/" + slug + ".pdf")
						os.chdir(ROOT + "/content")
	os.chdir(ROOT)

def del_tex2pdf():
	os.chdir('content')
	rootdir = os.getcwd()
	for d in os.listdir(rootdir):
		if d.startswith("tex2pdf"):
			local('rd /s /q ' + d)
	os.chdir(ROOT)

def publish(message,publish_drafts=False):
	try:
		if os.path.exists('output/drafts'):
			if not publish_drafts:
				local('rd /s /q "output/drafts"')
	except Exception:
		pass
	#clean()
	build()
	make_figs()
	make_source()
	del_tex2pdf()
	local('git add -A')
	try:
		local('git commit -m"' + message + '"')
	except Exception:
		pass
	local('git push')
	local('ghp-import output')
	local('git push git@github.com:gcman/gcman.github.io.git gh-pages:master --force') # 5