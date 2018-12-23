import os,re

INDENT = 3

def word_to_date(date):
    date = date.split(" ")
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    M = str(month.index(date[1])+1)
    D = date[0]
    out = [date[2]]
    for x in [M,D]:
        if int(x) < 10:
            x = "0" + x
        out.append(x)
    return "-".join(out)

def post_heading(metadata):
    tags = ":" + ":".join(re.split(",\s?",metadata["tags"].strip())) + ":"
    S = ["\n" + "*" * INDENT + " " + metadata["title"] + "  " + tags]
    S.append(":PROPERTIES:")
    if "slug" in metadata:
        S.append(":EXPORT_FILE_NAME: {}".format(metadata["slug"]))
    if "date" in metadata:
        S.append(":EXPORT_DATE: {}".format(word_to_date(metadata["date"])))
    if "shorttitle" in metadata:
        S.append(":EXPORT_HUGO_CUSTOM_FRONT_MATTER: :shortitle " + "\"" + metadata["shorttitle"] + "\"")
    if "summary" in metadata:
        S.append(":EXPORT_DESCRIPTION: {}".format(metadata["summary"]))
    S.append(":END:")
    return "\n".join(S)

def headings(obj):
    heading = obj.group(0).strip().split(" ")
    count = len(heading[0])
    body = " ".join(heading[1:])
    return "\n" + "*" * (count+INDENT) + " " + body

def links(obj):
    name = obj.group(1).strip()
    link = obj.group(2).strip()
    return "[[" + link + "][" + name + "]]"

def convert(file):
    print("Converting {}".format(file))
    with open(file,"r") as f:
        content = f.read().split("\n\n")
    # get metadata
    metadata = {}
    data = content[0]
    data = data.split("\n")
    for x in data:
        cat,dt = x.strip().split(": ")
        metadata[cat] = dt
        # get main body
    content = "\n" + "\n".join(content[1:])
    # temporarily store bold
    content = re.sub(r"\*\*(.*)\*\*","STRONGGG\g<1>STRONGGG",content)
    # convert italic
    content = re.sub(r"\*(.*)\*","/\g<1>/",content)
    # convert bold
    content = re.sub(r"STRONGGG(.*)STRONGGG","*\g<1>*",content)
    # convert keybd/code
    content = re.sub(r"`(.*)`","~\g<1>~",content)
    # convert headings
    content = re.sub(r"\n\#(.*)",headings,content)
    # convert links
    content = re.sub(r"\[(.*)\]\((.*)\)",links,content)
    content = post_heading(metadata) + content
    content = re.sub(r"\t","",content)
    with open("new.org","a") as f:
        f.write(content)

files = sorted([f for f in os.listdir("./") if os.path.isfile(os.path.join("./", f)) if ".md" in f])
for file in files:
    convert(file)
