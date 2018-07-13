#!/usr/bin/env python
from __future__ import unicode_literals
from fabric.api import *
import fabric.contrib.project as project
import os
import os.path as path
import shutil
import sys
if sys.version_info < (3,0):
	import SocketServer
else:
	import socketserver as SocketServer
from datetime import datetime
import markdown2
from itertools import chain
from glob import iglob
from shutil import copyfile
from git import Repo
from pelican.server import ComplexHTTPRequestHandler
from contextlib import contextmanager
from subprocess import call,Popen,PIPE
import re
import fileinput
import io

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
title: {title}
date: {day} {month} {year}
category:
tags:
slug: {slug}
summary:
status: draft

"""
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

repo = Repo(path.dirname(__file__))
assert not repo.bare
shell("git add -A")
untracked = [path.basename(x) for x in [item.a_path for item in repo.index.diff(None)]]
staged = [path.basename(x) for x in [item.a_path for item in repo.index.diff("HEAD")]]
diff = untracked + staged

def ext(f):
	return path.splitext(f)[-1].lower()

def bare(f):
	return "".join(path.splitext(f)[:-1])

def remove_prefix(text, prefix):
	if text.startswith(prefix):
		return text[len(prefix):]
	return text

def rmdir(dirname):
	if os.path.isdir(dirname):
		shutil.rmtree(dirname)

def mkdir(dirname):
	if not path.exists(dirname):
		os.mkdir(dirname)

def clean():
	# Remove generated files
	if path.isdir(DEPLOY_PATH):
		keep = ["figures"]
		for subdir, dirs, files in os.walk(DEPLOY_PATH,topdown=True):
			dirs[:] = [d for d in dirs if d not in keep]
			for file in files:
				p = path.join(subdir,file)
				if ext(file) != ".pdf":
					os.remove(p)
		mkdir(DEPLOY_PATH)

def build():
	# Build local version of site
	shell('pelican -s pelicanconf.py')

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
	mkdir(OUTPUT_DIR)
	for subdir, dirs, files in os.walk(CONTENT_DIR):
		for file in files:
			if ext(file) == ".tex":
				if file in diff or not path.isfile(path.join(CONTENT_DIR,bare(file)+".pdf")):
					print("Creating figure from {}".format(file))
					os.chdir(CONTENT_DIR)
					shell("latexmk -shell-escape -pdf -quiet " + file)
					shell("latexmk -c")
					shell("pdfcrop " + bare(file) + ".pdf " + bare(file) + ".pdf")
					os.chdir(ROOT)
				if file in diff or not path.isfile(path.join(OUTPUT_DIR,bare(file)+".png")):
					print(path.join(OUTPUT_DIR,bare(file)+".png"))
					print("Creating PNG from {}".format(bare(file) + ".pdf"))
					commands.append("convert -quiet -density 800 -background none -antialias " 
						+ path.join(CONTENT_DIR,bare(file)+".pdf") 
						+ " -channel rgba -alpha on -quality 2500 -trim png32:" + path.join(OUTPUT_DIR,bare(file) + ".png"))
		break # Prevents digging into subdirectories
	for file in os.listdir(OUTPUT_DIR):
		if ext(file) == ".png":
			if not path.isfile(path.join(CONTENT_DIR, bare(file) + ".pdf")):
				print(path.join(CONTENT_DIR, bare(file) + ".pdf"))
				os.remove(path.join(OUTPUT_DIR,file))
	for file in os.listdir(CONTENT_DIR):
		if ext(file) in [".table",".gnuplot",".gz",".xdv"]:
			os.remove(path.join(CONTENT_DIR,file))
	for c in commands:
		shell(c)
	os.chdir(ROOT)

def make_source():
	os.chdir('content')
	rootdir = os.getcwd()
	for file in os.listdir(rootdir):
		if ext(file) == ".md":
			with open(file, "r") as f:
				data = markdown2.markdown(f.read(), extras=["metadata"]).metadata
				slug = data["slug"].lower()
				if "status" in data:
					status = data["status"].lower()
				else:
					status = None
			if status != "draft":
				OUTPUT_DIR = path.join(path.dirname(rootdir),"output/" + slug)
				PDF_DIR = path.join(OUTPUT_DIR,"../pdf")
				MD = path.join(OUTPUT_DIR, "src.md")
				PDF = path.join(OUTPUT_DIR,"post.pdf")
				with io.open(file, "r",encoding="utf-8") as f:
						lines = [line for line in f]
						empty = 0
						for i,line in enumerate(lines):
							if line == "\n":
								empty = i
								break
				if file in diff or not path.isfile(MD):
					print("Copying {}".format(file))
					with io.open(MD, "w", encoding="utf-8") as f:
						s = "---\n"
						f.write(s)
						for i,line in enumerate(lines):
							test_path = None
							if i == empty:
								f.write(s + "\n")
							else:
								if i not in [0,len(lines)-1] and all([lines[x] == "\n" for x in [i-1,i+1]]) and line[0] == "!":
									fig = re.search("(?<=[(])(.*)(?=[)])",line).group(0)
									fig_name = re.search("(?<=figures/)(.*)",fig).group(0)
									if "http" not in fig:
										priority = ["pdf","png",ext(fig_name)]
										for p in priority:
											if not test_path:
												if p == "pdf":
													test_path = path.join(path.join(rootdir,"figures"), bare(fig_name) + "." + p)
												else:
													test_path = path.join(path.dirname(rootdir),"/output/figures/" + bare(fig_name) + "." + p)
										if path.isfile(test_path):
											line = line.replace(fig,test_path)
								f.write(line)
				if file in diff or path.join(ROOT, "/content/extra/header.tex") in diff or not path.isfile(PDF):
					print("Building PDF from {}".format(file))
					shell("pandoc extra/default.yaml -H extra/header.tex --template extra/template.tex --listings "
						+ MD + " -o " + PDF)
					os.remove(MD)
				if file in diff or not path.isfile(MD):
					with io.open(MD, "w", encoding="utf-8") as f:
						s = u"\u2010\u2010\u2010\n"
						f.write(s)
						for i, line in enumerate(lines):
							if i == empty:
								f.write(s + "\n")
							else:
								f.write(line)
	os.chdir(ROOT)

def del_tex2pdf():
	os.chdir('content')
	rootdir = os.getcwd()
	for d in os.listdir(rootdir):
		if d.startswith("tex2pdf"):
			shell('-rm -rf ' + d)
	os.chdir(ROOT)

def euler(sol=None):
	CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"content/euler")
	call(["python3", os.path.join(CONTENT_DIR,"heatmap.py")])
	call(["python3", os.path.join(CONTENT_DIR,"get-solution-paths.py")])
	if sol:
		call(["python3.6", os.path.join(CONTENT_DIR,"runtime.py"), str(sol)])
	call(["python3", os.path.join(CONTENT_DIR,"build-solutions.py")])

def preview():
	try:
		if path.exists('output/drafts'):
			if not publish_drafts:
				shell('-rm -rf output/drafts')
	except Exception:
		pass
	build()
	make_figs()
	make_source()
	del_tex2pdf()

def commit(message):
	shell('git add -A')
	shell('git commit --allow-empty -m"' + message +'"')

def push():
	shell('git push')

def hard_push():
	push()
	shell('ghp-import output')
	shell('git push https://github.com/gcman/gcman.github.io.git gh-pages:master --force')

def publish(message):
	preview()
	commit(message)
	push()
	hard_push()