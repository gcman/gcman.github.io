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
from pelican.server import ComplexHTTPRequestHandler

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
def clean():
	"""Remove generated files"""
	if os.path.isdir(DEPLOY_PATH):
		shutil.rmtree(DEPLOY_PATH)
		os.makedirs(DEPLOY_PATH)

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

def make_source():
	os.chdir('content')
	rootdir = os.getcwd()
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			ext = os.path.splitext(file)[-1].lower()
			if ext == ".md":
				with open (file, "r") as f:
					data = markdown2.markdown(f.read(), extras=["metadata"]).metadata
					if "status" not in data or data["status"].lower() != "draft":
						slug = data["slug"].lower()
						out = os.path.join(os.path.dirname(os.getcwd()),"output")
						srcdir = os.path.join(out,"src")
						pdfdir = os.path.join(out,"pdf")
						os.makedirs(srcdir,exist_ok=True)
						os.makedirs(pdfdir,exist_ok=True)
						copyfile(file,os.path.join(srcdir,slug+".md"))
						local("pandoc extra/default.yaml -H extra/header.tex --template extra/template.tex "
							+ file + " -o " + "../output/pdf/" + slug + ".pdf")

def publish(message,publish_drafts=False):
	try:
		if os.path.exists('output/drafts'):
			if not publish_drafts:
				local('rd /s /q "output/drafts"')
	except Exception:
		pass
	clean()
	build()
	make_source()
	local('git add -A')
	try:
		local('git commit -m"' + message + '"')
	except Exception:
		pass
	os.chdrir("..")
	local('git push')
	local('ghp-import output')
	local('git push git@github.com:gcman/gcman.github.io.git gh-pages:master --force') # 5