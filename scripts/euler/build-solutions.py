import os
import json
import jinja2
import codecs
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT,"../../data/euler/")

with open(os.path.join(DATA_DIR,"problemData.json"),"r",encoding="utf-8") as f:
	DATA = json.load(f)

with open(os.path.join(DATA_DIR,"hrDifficulty.json"),"r",encoding="utf-8") as f:
	diff = {"m":"Medium","h":"Hard","a":"Advanced","e":"Expert"}
	lines = {}
	for line in f.readlines():
		dt = line.strip().split(",")
		lines[int(dt[0])] = dt[1]
	for i in range(1,max(lines.keys())+1):
		if i in lines:
			DATA[str(i)]["hrdifficulty"] = diff[lines[i]]
		else:
			DATA[str(i)]["hrdifficulty"] = "Easy"

for x in [y for y in DATA if "path" in DATA[y]]:
	dir = DATA[x]["path"]
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"solutions/" + dir + "/main.py")
	empty = 0
	comments = 0
	code = ""
	with open(path,"rt") as f:
		for line in f.readlines():
			code += line
			if "#" in line:
				comments += 1
			if line == "\n":
				empty += 1
	out = highlight(code,PythonLexer(),HtmlFormatter(linenos=True))
	DATA[x]["code"] = out
	DATA[x]["empty"] = str(empty)
	DATA[x]["comments"] = str(comments)
	DATA[x]["difficulty"] = DATA[str(x)]["difficulty"]

with open(os.path.join(DATA_DIR,"euler-problem-data.json"), 'w',encoding="utf-8") as f:
	json.dump(DATA, f,ensure_ascii=False,indent=4)
