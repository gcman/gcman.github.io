from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import io

EULER = {}

for i in range(1,626):
	print("Processing problem {}".format(i))
	url = urlopen("https://projecteuler.net/problem=" + str(i))
	html = BeautifulSoup(url,"html.parser")
	EULER[i] = {}
	EULER[i]["name"] = html.find('h2').text.strip()
	d = re.search("(?<=Difficulty rating: )(.*)(?=%)",html.find('h3').text.strip())
	if d:
		EULER[i]["difficulty"] = d.group(0).strip()
	for x in EULER[i]:
		print(EULER[i][x])

with open("euler-problem-metadata.json", 'w', encoding='utf-8') as f:
    json.dump(EULER, f, ensure_ascii=False,indent=4)