from fabric.api import *
import fabric.contrib.project as project
import os
import os.path as path
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
from contextlib import contextmanager

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
repo = Repo(path.dirname(__file__))
assert not repo.bare
diff = [path.basename(x) for x in [item.a_path for item in repo.index.diff(None)]]

def ext(f):
	return path.splitext(f)[-1].lower()

def bare(f):
	return f.strip(ext(f))

@contextmanager
def suppress_stdout():
	with open(os.devnull, "w") as devnull:
		old_stdout = sys.stdout
		sys.stdout = devnull
		try:  
			yield
		finally:
			sys.stdout = old_stdout

def shell(command):
	with suppress_stdout():
		local(command)

def remove_prefix(text, prefix):
	if text.startswith(prefix):
		return text[len(prefix):]
	return text

def clean():
	# Remove generated files
	if path.isdir(DEPLOY_PATH):
		keep = ["pdf","figures"]
		files = [x for x in os.walk(DEPLOY_PATH)][0]
		for file in files[2]:
			os.remove(path.join(DEPLOY_PATH,file))
		for dir in files[1]:
			if dir not in keep:
				shutil.rmtree(path.join(DEPLOY_PATH,dir))
		os.makedirs(DEPLOY_PATH,exist_ok=True)

def build():
	# Build local version of site
	local('pelican -s pelicanconf.py')
	# Workaround: renames README.txt to README.md
	f = path.join("output/README.txt")
	out = path.splitext(f)[0] + ".md"
	try:
		os.rename(f, out)
	except WindowsError:
		os.remove(out)
		os.rename(f, out)

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

def make_figs():
	CONTENT_DIR = path.abspath(path.join(__file__ ,"../content/figures"))
	OUTPUT_DIR =  path.abspath(path.join(__file__ ,"../output/figures"))
	commands = []
	os.makedirs(path.join(OUTPUT_DIR),exist_ok=True)
	for subdir, dirs, files in os.walk(CONTENT_DIR):
		for file in files:
			if ext(file) == ".tex":
				if file in diff or not path.isfile(path.join(CONTENT_DIR,bare(file)+".pdf")):
					print("Creating figure from {}".format(file))
					shell("latexmk -shell-escape -pdf -quiet " + file)
					shell("latexmk -c")
				if bare(file) + ".pdf" in diff or not path.isfile(OUTPUT_DIR+bare(file)+".png"):
					print("Creating PNG from {}".format(bare(file) + ".pdf"))
					commands.append("magick -quiet -density 400 -background none -antialias " 
						+ path.join(CONTENT_DIR,bare(file)+".pdf") 
						+ " -quality 1000 -trim " + path.join(OUTPUT_DIR,bare(file) + ".png"))
		break # Prevents digging into subdirectories
	for file in os.listdir(OUTPUT_DIR):
		if ext(file) == ".png":
			if not path.isfile(path.join(CONTENT_DIR + bare(file) + ".pdf")):
				os.remove(path.join(OUTPUT_DIR,file))
	for c in commands:
		shell(c)
	os.chdir(ROOT)

def make_pdfs():
	os.chdir('content')
	rootdir = os.getcwd()
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			if ext(file) == ".md":
				with open(file, "r") as f:
					data = markdown2.markdown(f.read(), extras=["metadata"]).metadata
					slug = data["slug"].lower()
				out = path.join(path.dirname(rootdir),"output")
				pdfdir = path.join(out,"pdf")
				os.makedirs(pdfdir,exist_ok=True)
				if file in diff or path.join(ROOT, "/content/extra/header.tex") in diff or not path.isfile(path.join(pdfdir,slug+".pdf")):
					print("Building PDF from {}".format(file))
					shell("pandoc extra/default.yaml -H extra/header.tex --template extra/template.tex --listings "
						+ file + " -o " + "../output/pdf/" + slug + ".pdf")
	os.chdir(ROOT)

def del_tex2pdf():
	os.chdir('content')
	rootdir = os.getcwd()
	for d in os.listdir(rootdir):
		if d.startswith("tex2pdf"):
			shell('rd /s /q ' + d)
	os.chdir(ROOT)

def publish(message,publish_drafts=False):
	try:
		if path.exists('output/drafts'):
			if not publish_drafts:
				shell('rd /s /q "output/drafts"')
	except Exception:
		pass
	clean()
	build()
	make_figs()
	make_pdfs()
	del_tex2pdf()
	shell('git add -A')
	try:
		shell('git commit -m"' + message + '"')
		print("Committing {}".format(message))
	except Exception:
		pass
	shell('git push')
	shell('ghp-import output')
	local('git push git@github.com:gcman/gcman.github.io.git gh-pages:master --force')