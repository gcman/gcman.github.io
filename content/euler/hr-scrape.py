from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import io

for i in range(1,2):
	print("Processing problem {}".format(i))
	num = ""
	for j in range(3-len(str(i))):
		num += "0"
	num += str(i)
	url = urlopen("https://www.hackerrank.com/contests/projecteuler/challenges/euler" + num)
	html = BeautifulSoup(url,"html.parser")
	print(html)
	