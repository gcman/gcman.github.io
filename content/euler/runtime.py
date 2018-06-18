import os
from subprocess import run,PIPE
import json
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))

with open("euler-problem-data.json","r",encoding="utf-8") as f:
	DATA = json.load(f)

with open("euler-input.csv","r") as f:
	INPUT = {}
	for line in f.readlines():
		data = line.strip().split(",")
		INPUT[str(data[0])] = "\n".join(data[1:])

def time(n,runs=100):
	ans,time = compute_time(n,runs)
	if str(n) not in DATA:
		DATA[str(n)] = {}
	DATA[str(n)]["time"] = time
	return "The answer {} was computed over {} runs in {} ms per run.".format(ans,runs,time)

def compute_time(n,runs=100):
	if str(n) not in INPUT:
		return "Problem {} has no given test data.".format(n)
	path = os.path.join(os.path.abspath(__file__),"..//solutions//") + DATA[str(n)]["path"] + "//main.py"
	path = path.replace("\\","//")
	os.chdir(r"c://cygwin64//bin")
	cmd = ["bash", "-c", "time python " + path]
	test_case = INPUT[str(n)]
	TIME = 0
	for i in range(runs):
		print("Performing problem {}, run {}.".format(n,i+1),end="\r")
		sys.stdout.flush()
		p = run(cmd,input=test_case,stdout=PIPE, stderr=PIPE,encoding="ascii")
		time = p.stderr.split("\n")
		for j in range(2,4):
			t = time[j].split("\t")[1]
			mins = t.split("m")
			ms = 1000*float(mins[1].split("s")[0])
			mins = 60000*float(mins[0])
			TIME += ms + mins
	return p.stdout.strip(),str(int(TIME/runs))

n = int(input())
print(time(n))

with open(os.path.join(ROOT,"euler-problem-data.json"),"w",encoding="utf-8") as f:
	json.dump(DATA, f, ensure_ascii=False,indent=4)