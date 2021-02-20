
import os
import sys
import csv
import glob
import pandas as pd
import numpy as np
import sys
import simplejson
reload(sys)
sys.setdefaultencoding('utf8')

#!/usr/bin/env python
# -*- coding: utf-8 -*- 


#Making a single list from the variable catalogue file.
path =r'/home/hema/Desktop/sample/variable_catalogue'
filenames = glob.glob(path + "/*.xlsx")
variable1=[]
for file in filenames: 
	xl_file = pd.ExcelFile(file)
	xlsx = pd.ExcelFile(xl_file)
	variable_sheets = []
	for sheet in xlsx.sheet_names:
		variable_sheets.append(xlsx.parse(sheet))
		for df in variable_sheets:
			df1=df.dropna(axis=1, how='all')
		variable_sheets.append(df1)
	variable1.append(variable_sheets)


#print len(df1)	
#print df1
#print type(df1)

#print variable1
#print type(variable1)
flat_list1=[]
flat_list=[]
for sublist in variable1:
    flat=[]
    for item in sublist:
	ab=item.dropna()
        flat.append(ab)
    flat_list.append(flat)
flat_list1.append(flat_list)
#print flat_list1
#print type(flat_list[0][0][0])
#print len(flat_list[0][0])
#print type(flat_list)	

'''
#with open("singlelist.txt") as dataFile:
dataFile = open('singlelist.txt', 'r')
data = dataFile.readlines()
#print data[1:]

cars_dict = {}
for car in flat_list1:  
    cars_dict[car[0]] = car[1:]  
#print cars_dict


for line in data:
    #print line
#line = map(int, line.split())  #convert the text data to integers
    key, value = line[0], line[1:]
    items[key] = value
    #items.update({key: value})
#print items



#Write to csv file.
with open("singlelist1.csv","w") as f:
    wr = csv.writer(f)
    wr.writerows(flat_list1)


'''

import os
from collections import Counter
import glob

def word_frequency(fileobj, words):
    """Build a Counter of specified words in fileobj"""
    # initialise the counter to 0 for each word
    ct = Counter(dict((w, 0) for w in words))
    file_words = (word for line in fileobj for word in line.split())
    filtered_words = (word for word in file_words if word in words)
    return Counter(filtered_words)


def count_words_in_dir(dirpath, words, action=None):
    """For each .txt file in a dir, count the specified words"""
    for filepath in glob.iglob(os.path.join(dirpath, '*.txt')):
        with open(filepath) as f:
            ct = word_frequency(f, words)
            if action:
                action(filepath, ct)


def print_summary(filepath, ct):
    words = sorted(ct.keys())
    counts = [str(ct[k]) for k in words]
    print('{0}\n{1}\n{2}\n\n'.format(
        filepath,
        ', '.join(words),
        ', '.join(counts)))
    

words = set(['PREG', 'alcohol', 'wine', 'beer', 'mother', 'father', 'self report', 'teacher'])
count_words_in_dir('./', words, action=print_summary)















'''

#Finding word frequency
import nltk
import os
import re

#os.chdir("/home/hema/Desktop/sample/variable_catalogue")
filename="singlelist.txt"
textfile=open(filename,"r")
#print textfile
inputString=textfile.read()
word_list=re.split('\s+',file(filename).read().lower())



#spits out number of words in the textfileword_list.count('inflation')
a=word_list.count('alcohol')
print a
#spits out number of times 'inflation' occurs in the textfile
word_list.count('jobs')
word_list.count('output')




#Merging csv files
import glob
import pandas as pd

path =r'/home/hema/Desktop/sample'
allFiles = glob.glob(path + "/*.xlsx")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
print list_
#print frame


import sys
import csv
import glob
import pandas as pd

# get data file names
path =r'/home/hema/Desktop/sample/variable_catalouge'
filenames = glob.glob(path + "/*.xlsx")

dfs = []

for df in dfs: 
    xl_file = pd.ExcelFile(filenames)
    df=xl_file.parse('Sheet1')
    dfs.concat(df, ignore_index=True)
#print dfs


import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
#print files

files_xls = [f for f in files if f[-3:] == 'xlsx']
print files_xls

df = pd.DataFrame()

for f in files_xls:
    data = pd.read_excel(f, 'Sheet6')
    df = df.append(data)
#print df





#Merge excel files.Based at the University of Bristol, the ALSPAC is a world-leading birth cohort study. Between April 1991 and December 1992 more than 14,000 pregnant women were recruited into the study and these women (some of whom had two pregnancies or multiple births during the recruitment period), the children arising from the pregnancy, and their partners have been followed up intensively over two decades.

import numpy as np
import pandas as pd
import glob
all_data = pd.DataFrame()
for f in glob.glob("*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# now save the data frame
writer = pd.ExcelWriter('Sheet2.xlsx')
all_data.to_excel(writer,'sheet1')
writer.save() 

import pandas as pd

xlsx = pd.ExcelFile('Biological samples variable names.xlsx')
df = pd.read_excel(xlsx,  'Child')
df1 = pd.read_excel(xlsx,  'Ch Metabolomics')
df2 = pd.read_excel(xlsx,  'Mother')
df3 = pd.read_excel(xlsx,  'M Metabolomics')
df4 = pd.read_excel(xlsx,  'Father')

bigdata = pd.concat([df, df1, df2, df3, df4], ignore_index=True)
#print bigdata
bigdata1 = bigdata.to_csv('out.csv')
'''
