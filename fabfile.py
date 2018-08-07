import os
from fabric import api
from yaml import load,dump
from subprocess import call
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

ROOT = os.path.abspath(os.path.dirname(__file__))
EULER_CONTENT_DIR = os.path.join(ROOT,"content/blog/euler/")
EULER_DATA_DIR = os.path.join(ROOT,"data/euler/")

def load_euler_data():
    with open(os.path.join(EULER_DATA_DIR,"problemData.yaml"),"r") as f:
	return load(f)

def save_euler_data(data):
    with open(os.path.join(EULER_DATA_DIR,"problemData.yaml"), 'w') as f:
	dump(data,f)
        
def build_solutions():
    DATA = load_euler_data()
    with open(os.path.join(EULER_DATA_DIR,"hrDifficulty.yaml"),"r") as f:
	dt = load(f)
    diff = {"m":"Medium","h":"Hard","a":"Advanced","e":"Expert"}
    for i in range(1,max(dt.keys())+1):
	DATA[str(i)]["hrdifficulty"] = diff[dt[i]] if i in dt else "Easy"
    for x in [y for y in DATA if "path" in DATA[y]]:
	dir = DATA[x]["path"]
        path = os.path.join(ROOT,"scripts/euler/euler-solutions/" + dir + "/main.py")
        empty,comments,code = 0,0,""
	with open(path,"rt") as f:
	    for line in f.readlines():
                code += line
                if "#" in line:
                    comments += 1
                elif line == "\n":
                    empty += 1
	DATA[x]["code"] = highlight(code,PythonLexer(),HtmlFormatter(linenos=True))
	DATA[x]["empty"] = str(empty)
	DATA[x]["comments"] = str(comments)
    save_euler_data(DATA)

def get_solution_paths():
    DATA = load_euler_data()
    solved = []
    for file in os.listdir(EULER_CONTENT_DIR):
	num = None
	try:
	    num = int(file.split(".")[0])
	except ValueError as err:
		pass
	if num:
	    solved.append(str(num))
    for file in os.listdir(os.path.join(ROOT,"scripts/euler/euler-solutions/")):
	num_cand = file.split(".")[0]
	if num_cand in solved:
	    DATA[num]["path"] = file
    save_euler_data(DATA)

def euler(sol=None):
    get_solution_paths()
    if sol:
	call(["python3.6", os.path.join(ROOT,"scripts/euler/runtime.py"), str(sol)])
    build_solutions()
