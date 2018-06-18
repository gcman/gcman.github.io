from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import io

with open("euler-problem-metadata.json","r",encoding="utf-8") as f:
	DATA = json.load(f)

for i in range(1,626):
	print("Processing problem {}".format(i))
	url = urlopen("https://projecteuler.net/problem=" + str(i))
	html = BeautifulSoup(url,"html.parser")
	if i not in DATA:
		DATA[i] = {}
	DATA[i]["name"] = html.find('h2').text.strip()
	d = re.search("(?<=Difficulty rating: )(.*)(?=%)",html.find('h3').text.strip())
	if d:
		DATA[i]["difficulty"] = d.group(0).strip()

with open("euler-problem-data.json", 'w', encoding='utf-8') as f:
	json.dump(DATA, f, ensure_ascii=False,indent=4)