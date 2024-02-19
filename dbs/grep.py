# coding=utf-8
from os import listdir
import tok
#1 make shorten line to words 
#2 search all store files 
mylist = []
def line(q):
    for filename in listdir("/var/www/store/texts"):
        with open('/var/www/store/texts/'+filename, 'r') as f:
            for line in f.readlines():
#            for i, line in enumerate(f):
                lineclean=tok.tak(line.strip())
                qclean=tok.tak(q)
                if not lineclean:
                    continue
                linecleanlist=lineclean.split()
                qcleanlist=qclean.split()
                for ql in qcleanlist:                                    
                    if ql in linecleanlist:
                        mylist.append('<b>'+filename+'</b>'+lineclean.replace(ql, "<span style='background:yellow'>"+ql+'</span>'))
    return mylist