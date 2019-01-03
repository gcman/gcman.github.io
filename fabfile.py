import os
import shutil
from fabric import api
from git import Repo
from yaml import load, dump
from subprocess import call
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

ROOT = os.path.abspath(os.path.dirname(__file__))
EULER_CONTENT_DIR = os.path.join(ROOT, "content/euler/")
EULER_DATA_DIR = os.path.join(ROOT, "data/euler/")

repo = Repo(ROOT)
assert not repo.bare
untracked = [os.path.basename(
    x) for x in [item.a_path for item in repo.index.diff(None)]]
staged = [os.path.basename(x)
          for x in [item.a_path for item in repo.index.diff("HEAD")]]
diff = untracked + staged


def ext(f):
    return os.path.splitext(f)[-1].lower()


def bare(f):
    return "".join(os.path.splitext(f)[:-1])


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def rmdir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)


def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)


def load_euler_data():
    with open(os.path.join(EULER_DATA_DIR, "problemData.yaml"), "r") as f:
        return load(f)


def save_euler_data(data):
    with open(os.path.join(EULER_DATA_DIR, "problemData.yaml"), 'w') as f:
        dump(data, f)


def build_solutions():
    DATA = load_euler_data()
    with open(os.path.join(EULER_DATA_DIR, "hrDifficulty.yaml"), "r") as f:
        dt = load(f)
    diff = {"m": "Medium", "h": "Hard", "a": "Advanced", "e": "Expert"}
    for i in range(1, max([int(x) for x in dt.keys()])+1):
        DATA[str(i)]["hrdifficulty"] = diff[dt[str(i)]
                                            ] if str(i) in dt else "Easy"
    for x in [y for y in DATA if "path" in DATA[y]]:
        dir = DATA[x]["path"]
        path = os.path.join(
            ROOT, "scripts/euler/euler-solutions/" + dir + "/main.py")
        empty, comments, code = 0, 0, ""
        with open(path, "rt") as f:
            for line in f.readlines():
                code += line
                if "#" in line:
                    comments += 1
                elif line == "\n":
                    empty += 1
        DATA[x]["code"] = highlight(
            code, PythonLexer(), HtmlFormatter(linenos=True))
        DATA[x]["empty"] = str(empty)
        DATA[x]["comments"] = str(comments)
    save_euler_data(DATA)


def get_solution_paths():
    DATA = load_euler_data()
    solved = []
    for file in os.listdir(EULER_CONTENT_DIR):
        num = None
        try:
            num = int(file.split(".")[0])
        except ValueError as err:
            pass
        if num:
            solved.append(str(num))
    for file in os.listdir(os.path.join(ROOT, "scripts/euler/euler-solutions/")):
        num_cand = file.split(".")[0]
        if num_cand in solved:
            DATA[num]["path"] = file
    save_euler_data(DATA)


def euler(sol=None):
    get_solution_paths()
    if sol:
        call(["python3.6", os.path.join(ROOT, "scripts/euler/runtime.py"), str(sol)])
    build_solutions()


def make_figures():
    CONTENT_DIR = os.path.join(ROOT, "figures/src")
    OUTPUT_DIR = os.path.join(ROOT, "figures/pdf")
    IMG_DIR = os.path.join(ROOT, "static/img")
    mkdir(OUTPUT_DIR)
    for subdir, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            REL_DIR = remove_prefix(subdir, CONTENT_DIR)[1:]
            REL_FILE = os.path.join(REL_DIR, file)
            if ext(file) == ".tex":
                if (file in diff or not os.path.isfile(os.path.join(os.path.join(OUTPUT_DIR, REL_DIR), bare(file)+".pdf"))) and not os.path.isfile(os.path.join(os.path.join(CONTENT_DIR, REL_DIR), bare(file)+".pdf")):
                    print("Building {}".format(REL_FILE))
                    mkdir(os.path.join(OUTPUT_DIR, REL_DIR))
                    mkdir(os.path.join(IMG_DIR, REL_DIR))
                    os.chdir(os.path.join(CONTENT_DIR, REL_DIR))
                    call(["latexmk", "-shell-escape", "-pdf", "-quiet", file])
                    call(["latexmk", "-c", bare(file)+".pdf"])
                    call(["pdfcrop", bare(file)+".pdf", bare(file)+".pdf"])
                    print("Creating PNG from {}".format(bare(REL_FILE)+".pdf"))
                    call("convert -quiet -density 800 -background none -antialias " + bare(file)+".pdf" +
                         " -channel rgba -alpha on -quality 2500 -trim png32:" + os.path.join(IMG_DIR, bare(REL_FILE)+".png"), shell=True)
                    os.rename(bare(file)+".pdf",
                              os.path.join(OUTPUT_DIR, bare(REL_FILE)+".pdf"))
            os.chdir(ROOT)


def preview():
    try:
        if os.path.exists("public"):
            call("rm -rf public", shell=True)
    except Exception:
        pass
    call("hugo", shell=True)
    make_figures()
    euler()


def push():
    call("ghp-import public --force --push --branch=master", shell=True)


def publish():
    preview()
    push()
    call("rm -rf public", shell=True)
