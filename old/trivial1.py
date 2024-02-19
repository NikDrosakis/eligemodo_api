#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import random
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[ ]:


filename= 'dataset/geography.csv'
concap= pd.read_csv(filename)
n= len(concap.index)
df = pd.read_csv(filename).to_dict()


# In[ ]:


def trivial():   
    chosen=random.randint(0, n-1)
    chosenCountry=df['CountryName'][chosen]
    #print(df['CapitalName'][chosen])
    #give three more choices
    print("Which is the capital of: "+chosenCountry+"?")
    #create a dict without chosen adding chosen
    others=list(range(0, n-1))
    others.remove(chosen)
    otherChoices=random.sample(others, 3)
    otherChoices.append(chosen)
    random.shuffle(otherChoices)
    #enumerate
    my_dict = dict()
    for index,value in enumerate(otherChoices):
        my_dict[index+1] = value
    #print(my_dict)
    #shuffle whole list 
    for c in my_dict:
        print(str(c)+":"+df['CapitalName'][my_dict[c]])    
    chose = input()
    score['total'] +=1
    #ελέγχει αν το input είναι σωστό
    if str(my_dict[int(chose)])==str(chosen):
        score['correct'] +=1
        print("CORRECT")        
    else:
        score['mistake'] +=1
        print("MISTAKE")
    print(score)
    return score 
    
# Variable to keep the main loop running
running = True        
score={'correct':0,'mistake':0,'total':0}        
while running:
    score=trivial()
    rate=(score['correct']/score['total'])*100
    print("Score: "+str(rate)+"%") 
