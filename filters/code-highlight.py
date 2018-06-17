import panflute as pf

def action(elem,doc):
	if isinstance(elem,pf.CodeBlock):
		langs = set(["python"])
		S = [x for x in langs if x in elem.classes]
		if S:
			return pf.convert_text("<pre><code class='language-{}'>{}</code></pre>".format(S[0],elem.text))
		return pf.convert_text(elem.text)

def main(doc=None):
    return pf.run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()