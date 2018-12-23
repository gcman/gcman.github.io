import os

posts = {}
blog="""* Blog
:PROPERTIES:
:EXPORT_HUGO_SECTION: blog
:END:
** Blog Index
:PROPERTIES:
:EXPORT_FILE_NAME: _index
:END:
"""

with open("2018_02_04_harmonic-binomial.md","r") as f:
    content = "\n".join(f.read().split("\n\n")[1:])
    re.sub(content,"#","*")
    metadata = {}
    for l in f:
        if l.strip():
            cat,dt = l.strip().split(":")
            metadata[cat] = dt
        else:
          break
