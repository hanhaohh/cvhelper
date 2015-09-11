#!/usr/bin/python
# -*- coding: utf-8 -*-
from basic import word_tokenize,stem,clean_html,remove_punc,plural_to_sing,rm_stop_words
from linkedlist import *
from config import DOWNLOAD_DIR 
from os import listdir
import os,re
import cPickle as pickle 
# from sklearn.feature_extraction.text import CountVectorizer

def create_index():
	file_names = listdir(DOWNLOAD_DIR)
	i = 0 

	total = [] 
	for name in file_names[1:]:
		i = i + 1
		File = open(DOWNLOAD_DIR+"/"+name,"r")
		raw_text = remove_punc(clean_html(File.read()))
		text = word_tokenize(raw_text)
		File.close()
		#this is to remove punctuation,stop words, plural to single, upppercase to lowercase 
		text_stemmed = [((plural_to_sing(word.lower()))) for word in text] 
		text_stemmed = [rm_stop_words(k) for k in text_stemmed if rm_stop_words(k) is not ""]
		unique_tokens = list(set(text_stemmed))
		tokens = [ (j,name,text_stemmed.count(j)) for j in unique_tokens ]
		total.extend(tokens)
	pickle.dump( total, open( "index.p", "wb" ) )
def create_inverted_index():
	index = pickle.load( open( "index.p", "rb" ) )
	dic = {}
	words = [i[0] for i in index]
	for i in set(words):
		dic[i] = LinkedList()
	for i in index:
		dic[i[0]].append((Node(i[0],i[1],i[2])))
	return dic 
ll = create_inverted_index()["python"]
print ll.get_doc_ID()