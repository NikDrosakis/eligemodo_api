# coding=utf-8
import nltk
import io
import os
import sys, json
# import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('gutenberg')
#nltk.download("punkt")
#nltk.download('averaged_perceptron_tagger')
from urllib import request
from nltk.corpus import gutenberg
# print(gutenberg.fileids())
#nltk.download('stopwords')
#nltk.download('punkt')
#q = sys.argv[1]
#filename = 'telika_eleftheria.txt'

# οκ αφαίρεση stopwords
# ok αφαίρεση σημείων στίξης
# ok αφαίρεση αριθμών
# ok αφαίρεση λέξη του ενός γράμματος
# οκ tag and save in newfile and tags in
# οκ αφαίρεση επιρρήματα και αντωνυμιες
# δημιουργία αρχικού αρχείου με tagged λέξεις και index στη db, σημαντικό να υπάρχει η σειρά του tag, ίσως και 5-6 λεξεις πριν και μετά
# useless in mongo
# αντί εργαλείο να βγάζει useless γιατί δεν ταγκάρω εγώ τη χρήσιμη για να ψάχνει η javascript 
# keyup γράψιμο ταγκαρισμένης λέξης (πρώτο γράμμα tag) στο space αναζήτηση στο wikipedia για αρχή
    
def raw(filename):
    return repr(open(filename, 'rb').read().decode('utf8').replace("\n", " "))
    
def tak(line):    
    all_stopwords = stopwords.words('english')
    all_stopwords.extend(stopwords.words('greek'))
    filtered_list = ["είναι","και","Και", "κι", "Κι",'άλλο','ναι','όχι','εγώ','εσύ','αυτός','εκείνος','αυτοί','ούτε','ποτέ','αλλά','Στο','στον','σου','απ','της','στα','τους','των','τα','οι','πια','έστω','είπε','μία','γιατί','όσα','κάθε','ένα','μια','κάποιος','κάποιοι','όλους','αυτούς','λένε']
    all_stopwords.extend(filtered_list)
    # print(nltk.tokenize.punkt)
    # print(all_stopwords)
    # print(tokens_without_sw)
    # print(all_stopwords)
    # all_stopwords.remove('not')
    # text1.similar("monstrous")
    # λέξεις στη ρίζα τυος porter = PorterStemmer()
    # stemmed = [porter.stem(word) for word in tokens]
    # tokeinze
    # text_tokens = word_tokenize(raw)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    # text_tokens = tokenizer.tokenize(raw)
    text_tokens = filterarray(tokenizer.tokenize(line))
    # print(len(text_tokens))
    # tagged = nltk.pos_tag(text_tokens)
    # tokens_without_sw = [word for word in text_tokens if word.isalpha()]
    tokens_without_stopwords = [word for word in text_tokens if not word in all_stopwords]
    #print(str(len(tokens_without_stopwords)) + " tagged words")
    #print((len(tokens_without_stopwords)/len(raw.split(" ")))*100)
    #print("%")
    filtered = (" ").join(tokens_without_stopwords)
    return filtered
    
def tik(q):    
    all_stopwords = stopwords.words('english')
    all_stopwords.extend(stopwords.words('greek'))
    filtered_list = ["και","Και", "κι", "Κι",'άλλο','ναι','όχι','εγώ','εσύ','αυτός','εκείνος','αυτοί','ούτε','ποτέ','αλλά','Στο','στον','σου','απ','της','στα','τους','των','τα','οι','πια','έστω','είπε','μία','γιατί','όσα','κάθε','ένα','μια','κάποιος','κάποιοι','όλους','αυτούς','λένε']
    all_stopwords.extend(filtered_list)
    # print(nltk.tokenize.punkt)
    # print(all_stopwords)
    # print(tokens_without_sw)
    # print(all_stopwords)
    # all_stopwords.remove('not')
    # text1.similar("monstrous")
    # λέξεις στη ρίζα τυος porter = PorterStemmer()
    # stemmed = [porter.stem(word) for word in tokens]
    # tokeinze
    # text_tokens = word_tokenize(raw)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    # text_tokens = tokenizer.tokenize(raw)
    text_tokens = filterarray(tokenizer.tokenize(raw(q)))
    # print(len(text_tokens))
    # tagged = nltk.pos_tag(text_tokens)
    # tokens_without_sw = [word for word in text_tokens if word.isalpha()]
    tokens_without_stopwords = [word for word in text_tokens if not word in all_stopwords]
    #print(str(len(tokens_without_stopwords)) + " tagged words")
    #print((len(tokens_without_stopwords)/len(raw.split(" ")))*100)
    #print("%")
    filtered = (" ").join(tokens_without_stopwords)
    return filtered

def filterarray(content):
    filtered = []
    for i in content:
        i = str(i)
        if not i.isdigit() and len(i) > 1:
            filtered.append(i)
    return filtered
    # return ["valid", "invalid"][content.count(" ") >= len(concept) // 2]

# create new file
def createnewfile(content):
    tag = 0
    key = True
    newfilename = filename.split('.')[0]
    while key:
        newfile = newfilename + "_" + str(tag) + ".txt"
        if not os.path.exists(newfile):
            with io.open(newfile, "w", encoding="utf-8") as f:
                f.write(content)
            f.close()
            key = False
        tag += 1

#createnewfile(filtered)
#print(filtered)
#sys.stdout.flush()
#result = {'success':'true','message':filtered};

#myjson = json.load(sys.stdin)
# Do something with 'myjson' object

#print 'Content-Type: application/json\n\n'
#print(json.dumps(result))    
#print(json.dump(result, sys.stdout))