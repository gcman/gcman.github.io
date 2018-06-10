import jinja2
import random
import os
import json

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=""))
HEAT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__) ,"../theme/templates"))
template = env.get_template(os.path.join(os.path.dirname(__file__),"heat.html"))

with open('euler-problem-data.txt') as dt:
	EULER = json.load(dt)

heat = []

options = {"dg": "complete","lg":"hackerrank-imperfect","y":"tle","g":"unsolved","b":"euler-only"}
with open('solved.txt') as f:
	solved = {}
	for line in f:
		idx,stat = line.strip().split(",")
		solved[int(idx)] = stat
for i in range(1):
	heati = []
	for j in range(5):
		heatj = []
		for k in range(20):
			num = i*100 + j*20 + k + 1
			if num in solved:
				status = solved[num]
			else:
				status = "g"
			heatk = {"num": str(num), "cls": options[status]}
			if status != "g":
				heatk["link"] = EULER[str(num)]["name"] + " (Difficulty: {}%)".format(EULER[str(num)]["difficulty"])
			heatj.append(heatk)
		heati.append(heatj)
	heat.append(heati)
with open(os.path.join(HEAT_DIR,"heatmap.html"),"w") as f:
	f.write(template.render(heat=heat))