import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))
CONTENT_DIR = os.path.join(ROOT,"../../content/blog/euler")
DATA_DIR = os.path.join(ROOT,"../../data/euler/")

with open(os.path.join(DATA_DIR,"problemData.json"),"r",encoding="utf-8") as f:
	DATA = json.load(f)

solved = {}
for file in os.listdir(CONTENT_DIR):
	num = None
	try:
		num = int(file.split(".")[0])
	except ValueError as err:
		pass
	if num:
		solved[num] = {"num":str(num)}

for file in os.listdir(os.path.join(ROOT,"solutions")):
	num = int(file.split("-")[0])
	if num in solved:
		DATA[str(num)]["path"] = file

with open(os.path.join(DATA_DIR,"problemData.json"), 'w',encoding="utf-8") as f:
	json.dump(DATA, f,ensure_ascii=False,indent=4)
