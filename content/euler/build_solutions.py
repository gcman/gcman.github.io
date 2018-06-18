import os
import json
import jinja2
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=""))
DIR = os.path.abspath(os.path.join(os.path.dirname(__file__) ,"../theme/templates"))
template = env.get_template(os.path.join(os.path.dirname(__file__),"euler-extra.html"))

solved = {}
for file in os.listdir(os.path.join(os.path.abspath(__file__),"../../")):
	if "euler-" in file:
		num = None
		try:
			num = int(file.split("-")[1].split(".")[0])
		except ValueError as err:
			pass
		if num:
			solved[num] = {"num":str(num)}

for file in os.listdir(os.path.join(os.path.abspath(__file__),"../solutions/")):
	num = int(file.split("-")[0])
	if num in solved:
		solved[num]["path"] = file

for x in solved:
	dir = solved[x]["path"]
	path = os.path.join(os.path.abspath(__file__),"../solutions/" + dir + "/main.py")
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
	solved[x]["code"] = out
	solved[x]["empty"] = str(empty)
	solved[x]["comments"] = str(comments)
	with open("euler-problem-metadata.json","r") as f:
		solved[x]["difficulty"] = json.load(f)[str(x)]["difficulty"]
	with open(os.path.join(DIR,"euler/"+str(x)+".html"),"w") as f:
		f.write(template.render(meta=solved[x]))

with open("extra-solution-data.json", 'w', encoding='utf-8') as f:
	json.dump(solved, f, ensure_ascii=False,indent=4)