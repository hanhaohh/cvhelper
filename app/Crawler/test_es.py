from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from os import listdir
from basic import *
from config import DOWNLOAD_DIR
es = Elasticsearch()
body={
    'query': {
        'match_all':{
        }
       		 }
	 }
a = es.count(index='hanhao',doc_type="linkedin",body = body)
print a