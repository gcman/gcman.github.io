import jinja2
import random

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=""))
template = env.get_template("heat.html")

heat = []
options = ["complete","hackerrank-imperfect","tle","unsolved","euler-only"]
for i in range(6):
	heati = []
	for j in range(4):
		heatj = []
		for k in range(25):
			idx = random.randint(0,4)
			heatk = {"num": str(i*100 + j*25 + k + 1), "cls": options[idx]}
			heatj.append(heatk)
		heati.append(heatj)
	heat.append(heati)
with open("heatmap.html","w") as f:
	f.write(template.render(heat=heat))