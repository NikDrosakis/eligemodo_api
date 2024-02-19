# coding=utf-8
import sys
import wikipedia
wikipedia.set_lang("el")
q = sys.argv[1]
def ask(q):
    suggestion=wikipedia.search(q, results = 10, suggestion = True)
    res=str(suggestion)+"\n"+str(wikipedia.summary(suggestion))
    return res
#print(res)
#sys.stdout.flush()