import jinja2
import random
import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))

env = jinja2.Environment(loader=jinja2.FileSystemLoader(ROOT))
HEAT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__) ,"../theme/templates"))

def save_data():
	with open(os.path.join(ROOT,"euler-problem-data.json"),"w",encoding="utf-8") as f:
		json.dump(DATA, f, ensure_ascii=False,indent=4)

with open(os.path.join(ROOT,'euler-problem-data.json'),"r",encoding="utf-8") as dt:
	DATA = json.load(dt)

heat = []

options = {"dg": "complete","lg":"hackerrank-imperfect","y":"tle","g":"unsolved","b":"euler-only"}
with open(os.path.join(ROOT,'heat-solved.csv')) as f:
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
				heatk["link"] = DATA[str(num)]["name"] + " (Difficulty: {}%)".format(DATA[str(num)]["difficulty"])
			DATA[str(num)]["num"] = str(num)
			heatj.append(heatk)
		heati.append(heatj)
	heat.append(heati)
with open(os.path.join(HEAT_DIR,"heatmap.html"),"w") as f:
	f.write(env.get_template("heat.html").render(heat=heat))
save_data()