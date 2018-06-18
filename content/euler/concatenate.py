import json
DATA = {}
for name in ["euler-problem-metadata.json","euler-runtime-data.json","extra-solution-data.json"]:
	with open(name,"r",encoding="utf-8") as f:
		tmp = json.load(f)
		for x in tmp:
			if x not in DATA:
				DATA[x] = {}
			for key in tmp[x]:
				DATA[x][key] = tmp[x][key]
with open("euler-problem-data.json","w",encoding="utf-8") as f:
	json.dump(DATA, f, ensure_ascii=False,indent=4)