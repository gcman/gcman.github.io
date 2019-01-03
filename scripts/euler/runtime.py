import os
import sys
from yaml import load, dump
from subprocess import run, PIPE

RUNS = 10
ROOT = os.path.join(os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__)))))
EULER_DATA_DIR = os.path.join(ROOT, "data/euler/")

with open(os.path.join(EULER_DATA_DIR, "problemData.yaml"), "r", encoding="utf-8") as f:
    DATA = load(f)

with open(os.path.join(ROOT, "scripts/euler/euler-input.csv"), "r") as f:
    INPUT = {}
    for line in f.readlines():
        data = line.strip().split(",")
        INPUT[str(data[0])] = "\n".join(data[1:])


def save_data():
    with open(os.path.join(EULER_DATA_DIR, "problemData.yaml"), "w", encoding="utf-8") as f:
        dump(DATA, f)


def time(n, runs=RUNS):
    if "path" not in DATA[str(n)] or str(n) not in INPUT:
        return "Problem {} has no given test data or no path to solution. Skipping.".format(n)
    else:
        ans, time, mem = compute_time(n, runs)
        if str(n) not in DATA:
            DATA[str(n)] = {}
        DATA[str(n)]["runtime"] = time
        DATA[str(n)]["memory"] = mem
        save_data()
        return "\nProblem: {}\nAnswer: {}\nRuns: {}\nTime (ms): {}\nPeak memory usage (KB): {}".format(n, ans, runs, time, mem)


def compute_time(n, runs):
    path = os.path.join(ROOT, "scripts/euler/euler-solutions/") + \
        DATA[str(n)]["path"] + "/main.py"
    cmd = ["/usr/bin/time", "--verbose", "python3.6", path]
    test_case = INPUT[str(n)]
    TIME = 0
    MEM = 0
    for i in range(runs):
        print("Performing problem {}, run {}.".format(n, i+1), end="\r")
        sys.stdout.flush()
        p = run(cmd, input=test_case, stdout=PIPE,
                stderr=PIPE, encoding="ascii")
        time = p.stderr.split("\n")
        t = time[4].split(":")
        mins = 60000*float(t[-2])
        ms = 1000*float(t[-1])
        TIME += mins + ms
        mem = float(time[9].split(":")[-1])
        MEM += mem
        return p.stdout.strip(), str(int(TIME/runs)), str(int(MEM/runs))


print(time(sys.argv[1]))
