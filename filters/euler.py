import panflute as pf
import os

def prepare(doc):
	for elem in doc.content:
		if isinstance(elem,pf.Header) and elem.identifier == "problem-statement":
			extra = []

def action(elem,doc):
	

def main(doc=None):
	return pf.run_filter(action, doc=doc) 

if __name__ == '__main__':
	main()