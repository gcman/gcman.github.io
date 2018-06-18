import panflute as pf
import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def action(elem,doc):
	if isinstance(elem,pf.CodeBlock):
		LANGS = {"python":PythonLexer()}
		if "include" in elem.classes:
			fn = os.path.join(os.path.dirname(os.path.dirname(__file__)),"content/" + elem.text)
			with open(fn,"rt") as f:
				raw = f.read()
		else:
			raw = elem.text
		S = [x for x in LANGS.keys() if x in elem.classes]
		if S:
			lexer = LANGS[S[0]]
			linenums = "number-lines" in elem.classes
			f = HtmlFormatter(linenos=linenums)
			return pf.convert_text(highlight(raw,lexer,f))
		return pf.convert_text(raw)

def main(doc=None):
    return pf.run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()