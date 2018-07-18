import jinja2
import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))

env = jinja2.Environment(loader=jinja2.FileSystemLoader(ROOT))
TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__) ,"../theme/templates"))

with open(os.path.join(ROOT,'euler-problem-data.json'),"r",encoding="utf-8") as dt:
	DATA = json.load(dt)

def save_data():
	with open(os.path.join(ROOT,"euler-problem-data.json"),"w",encoding="utf-8") as f:
		json.dump(DATA, f, ensure_ascii=False,indent=4)

def get_title(n):
	with open(os.path.join(os.path.dirname(ROOT), 'euler-' + str(n) + '.md'),"r") as f:
		title = f.readline().split(" - ")[1].strip()
	return title

for n in DATA:
	if "path" in DATA[n]:
		DATA[n]["name"] = get_title(int(n))

TABLE_DATA = sorted([DATA[d] for d in DATA if all([x in DATA[d] for x in ["num","name","difficulty","hrdifficulty","memory","runtime"]])], key=lambda x: int(x["num"]))

with open(os.path.join(TEMPLATE_DIR,"progress-table.html"),"w") as f:
	f.write(env.get_template("progress.html").render(data=TABLE_DATA))

save_data()