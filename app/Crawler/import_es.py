from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from os import listdir
from basic import word_tokenize,stem,clean_html,remove_punc,plural_to_sing,rm_stop_words,get_loc_job_title
from config import DOWNLOAD_DIR
es = Elasticsearch("localhost")
import cPickle as pickle 
def create_index():
	file_names = listdir(DOWNLOAD_DIR)
	i = 0 
	total = [] 
	for name in file_names[1:]:
		i = i + 1
		File = open(DOWNLOAD_DIR+"/"+name,"r")
		txt = File.read()
		raw_text = remove_punc(clean_html(txt))
		title,job,loc = get_loc_job_title(txt)
		text = word_tokenize(raw_text)
		File.close()
		#this is to remove punctuation,stop words, plural to single, upppercase to lowercase 
		text_stemmed = [((plural_to_sing(word.lower()))) for word in text] 
		text_stemmed = [rm_stop_words(k) for k in text_stemmed if rm_stop_words(k) is not ""]
		content =  " ".join(text_stemmed)
		a =  [title,job,loc,content]
		total.append(a)
	return total
def import_es(docs):
	count = len(docs)
	actions = []
	j  = 0 
	while (j < count):
		action = {
	        "_index": "docs",
	        "_type": "linkedin",
	        "_id": j + 1,
	        "_source": {
	              "titile":docs[j][0],
	              "job":docs[j][1],
	              "loc": docs[j][2],
	              "content":docs[j][3],
	              "time": datetime.now()
	              }
	        }
		actions.append(action)
	  	j += 1
	helpers.bulk(es, actions)
docs =  create_index()
import_es(docs)
