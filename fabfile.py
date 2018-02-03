from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver
from datetime import datetime
import livereload
import webbrowser

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
PORT = 8000
TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category:
:slug: {slug}
:summary:
:status: draft


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

	class AddressReuseTCPServer(SocketServer.TCPServer):
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
def publish():
	"""Publish to production via rsync"""
	local('pelican -s publishconf.py')
	project.rsync_project(
		remote_dir=dest_path,
		exclude=".DS_Store",
		local_dir=DEPLOY_PATH.rstrip('/') + '/',
		delete=True,
		extra_opts='-c',
	)

def gh_pages():
	"""Publish to GitHub Pages"""
	rebuild()
	local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))

def post(title):
	today = datetime.today()
	slug = title.lower().strip().replace(' ', '-')
	f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
		today.year, today.month, today.day, slug)
	t = TEMPLATE.strip().format(title=title,
								hashes='#' * len(title),
								year=today.year,
								month=today.month,
								day=today.day,
								hour=today.hour,
								minute=today.minute,
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
	server.watch('../content/*.rst',  # 5
		livereload.shell('pelican -s ../pelicanconf.py -o ../output'))  # 6
	server.watch('../pelican-themes/cebong/',  # 7
		livereload.shell('pelican -s ../pelicanconf.py -o ../output'))  # 8
	server.watch('*.html')  # 9
	server.watch('*.css')  # 10
	server.serve(liveport=35729, port=port)  # 11

def enter_dns_file():  # 1
	with open('output/CNAME', 'w') as f:
		f.write('gautammanohar.com')