import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT,"euler-problem-data.json"),"r",encoding="utf-8") as f:
	DATA = json.load(f)

solved = {}
for file in os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
	if "euler-" in file:
		num = None
		try:
			num = int(file.split("-")[1].split(".")[0])
		except ValueError as err:
			pass
		if num:
			solved[num] = {"num":str(num)}

for file in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"solutions")):
	num = int(file.split("-")[0])
	if num in solved:
		DATA[str(num)]["path"] = file

with open(os.path.join(ROOT,"euler-problem-data.json"), 'w',encoding="utf-8") as f:
	json.dump(DATA, f,ensure_ascii=False,indent=4)