#############################ALSPAC data###################################################################
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
from collections import Counter
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])

pd.set_option('display.height',1000000)
pd.set_option('display.max_rows',1000000)
pd.set_option('display.max_columns',1000000)
pd.set_option('display.width',1000000)
pd.set_option('display.max_colwidth', -1)
    


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

#print type(variable1)

#ab=pd.describe_option('variable1')
#print ab
#Remove NA's from the list.

flat_list1=[]
flat_list=[]
for sublist in variable1:
    flat=[]
    for item in sublist:
	ab=item.dropna()
        flat.append(ab)
    flat_list.append(flat)
flat_list1.append(flat_list)
#print type(flat_list1)
#print flat_list1
#print len(flat_list1[0])
#print len(flat_list1[0][0])
#print len(flat_list1[0][0][0])

''' /home/hema/Desktop/sample/variable_catalogue
#Write a list into a csv file.
with open("singlelist.csv","w") as f:
    wr = csv.writer(f)
    wr.writerows(flat_list1)
'''
#Write a list into a txt file.
thefile = open('test.txt', 'w')
for item in flat_list1:
  thefile.write("%s\n" % item)

######################################################################################################
from collections import defaultdict
 
d = defaultdict(list)
with open('test.txt') as f:
  for line in f:
    parts = line.strip().split()
   
    
    #parts = line.split("\t")
    d[parts[2]] += parts[3:]
#print d.values()


'''
f = open('singlelist.txt', 'r')
keyword = f.readlines()
#print keyword

keylist = []
for value in keyword:
	keylist.append(value.strip().split('\t'))
'''


#Reading a keywordsfile.
keywordfile = open('keywordsFile1.txt', 'r')
keywordfile1 = keywordfile.readlines()
#print keywordfile1

keywordlist = []
for values in keywordfile1:
	keywordlist.append(values.strip().split('\t'))
del keywordlist[0]
#print keywordlist
keywordlist1 = []
for i in keywordlist:
	i.pop(0)
	keywordlist1.append(i)
#print keywordlist1
#print keywordlist[0][2]

import re

for i in keywordlist1:
	i.insert(0, ("dictvalues"))
	#i[0].replace("'", "")
#print keywordlist1
keywordlist2=[]

for j in keywordlist1:
	ad=('[{}]'.format(', '.join(j)))
	#print ad
	#for k in j:	
	keywordlist2.append(ad)
	#print abcde
	#abcde1 = ("[" + j[0].strip() + "]")
	#keywordlist2.update({abcde: j[1:]})
#print keywordlist2
from operator import add
key=[]
for i in keywordlist2:
	abcd = i.replace("'", "")
	list3 = map(add, keywordlist1, abcd)
#print key
	#print list3


'''

i = 0
keyworddict = {}
#list = []
for i in range(0, len(keywordlist)):
	s=keywordlist[i]
	for key, val in d.iteritems():
		#ab/home/hema/Desktop/sample/variable_catalogue = ' '.join(val)
		for va in val:
			#print va
			if s in va:
			
				keyworddict.update({key: val})
				i = i + 1
#print keyworddict
#print i
'''

	

import re

keyworddict1 = {}

for key, val in d.iteritems():
#for i in range(0, len(d)):
	#for j in range(0, len(keywordlist[0])):
	dictvalues = ' '.join(val)
	def lines_with_words(dictvalues, word1, word2):
	#def lines_with_words(dictvalues, lists):
		#c = lists.split("")
		#for i in keywordlist[0][1:]:
				
		if re.search(r"\b" + word1 + r"\b", dictvalues, re.IGNORECASE) and re.search(r"\b" + word2 + r"\b", dictvalues, re.IGNORECASE):
		#for k in keywordlist[0]:
			#if re.search(k, ab):
			keyworddict1.update({key: dictvalues})
	
	params1 = [[dictvalues, 'PREG.*', 'alcohol.*'], [dictvalues, 'PREG.*', 'beer.*'], [dictvalues, 'PRES.*', 'alcohol.*'], [dictvalues, 'alcohol.*', 'week.*'], [dictvalues, 'wine.*', 'week.*'], [dictvalues, 'beer.*', 'week.*']]
	for params in keywordlist1:
		abcde = params[0].strip()
		lines_with_words(*params)
'''			
	lines_with_words(dictvalues, 'PREG.*', 'alcohol.*')
	lines_with_words(dictvalues, 'PREG.*', 'wine.*')
	lines_with_words(dictvalues, 'PREG.*', 'beer.*')
	lines_with_words(dictvalues, 'PRES.*', 'alcohol.*')
	lines_with_words(dictvalues, 'alcohol.*', 'week.*')
	lines_with_words(dictvalues, 'Wine.*', 'week.*')
	lines_with_words(dictvalues, 'Beer.*', 'week.*')
	#lines_with_words(dictvalues, 'PRES.*', 'coffee.*')
	#lines_with_words(dictvalues, 'PRES.*', 'milk.*')
	#lines_with_words(dictvalues, 'PRES.*', 'tea.*')
	#lines_with_words(dictvalues, 'PRES.*', 'cola.*')
		#if keywordlist[0][j] in ab:
		#if ab.find(keywordlist[0][j]):snipers
			#keyworddict1.update({key: ab})
'''
#print keyworddict1
#print len(keyworddict1)

#!/usr/bin/python
def findDouble(inputfilename):
	''' a function that finds all double occurences of a word'''
	input = open("/home/hema/Desktop/sample/variable_catalogue/keywordsFile1.txt",'r')
	filelist = input.readlines() # this will import all lines as elements in a list
	print filelist
	#input.close()
	import re
	double = re.compile(r'(\b\w+) \1\b') # regular expression for matching all double words
	strfilename = "" # placeholder for str converted filelist, should it be outside loop?
	findnewline = re.compile(r'\n')
	for elements in range(len(filelist)): #remove all "\n" and make list to single str
		strfilename += str(filelist[elements])
		findnewline.sub(' ', strfilename)
		
	result = double.findall(strfilename)
	return result

#Write dictionary (keyworddict1) into a txt file (file.txt).
import json

with open('Variablefile.txt', 'w') as file:
     file.write(json.dumps(keyworddict1))

 	
'''


i = 0
c={}
for key, val in d.iteritems():
	for va in val:
		if va.lower() == "preg.*".lower():
			
		#if va == "preg*":	
		
		#print ({key: val})
		
			c.update({key: val})
			i = i + 1
print c
print i





##############################################################################################################

#Finding word frequency
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
        

words = set(['PREG', 'alcohol', 'wine'])
count_words_in_dir('./', words, action=print_summary)



#################################################################################################################


''' 


