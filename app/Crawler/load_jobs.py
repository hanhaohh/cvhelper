#!/usr/bin/env python
#coding:utf-8

import urllib2
import re
import threading
import time
import random
from basic import save_data
from config import checkedProxyList,accounts,DOWNLOAD_DIR
from Queue import Queue
import requests

class DownloadJob(threading.Thread):
    def __init__(self,job_queue,thread_id=''):
        threading.Thread.__init__(self)
        self.timeout = 5
        self.thread_id = thread_id 
        self.job_queue =  job_queue
        self.EXIT_FLAG = 0
        self.session = requests.session()
        print "init"
    def opener(self,url):
        cookies = urllib2.HTTPCookieProcessor()
        randomCheckedProxy = random.choice(checkedProxyList) #随机取一组代理服务器
        proxyHandler = urllib2.ProxyHandler({"http" : randomCheckedProxy})
        opener = urllib2.build_opener(cookies,proxyHandler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')]
        urllib2.install_opener(opener)
        try:
            data = opener.open("https://"+url,timeout=self.timeout).read()
        except:
            data = ""
        save_data(data,DOWNLOAD_DIR+str(int(time.time())))
        if (data) == "":
            return False
        else:
            pass
        return data
    
    def download(self):
        url = self.job_queue.get()
        time.sleep(random.randint(6,12)) 
        while not self.opener(url):
             self.opener(url)
   
    def run(self):
        print "start running",self.thread_id
        while not self.EXIT_FLAG:
            self.download()
    def stop(self):
        self.EXIT_FLAG = 1

if __name__ == "__main__":
    threads = []
    process_id = 1
    #read in the jobs and put them in the queue
    File = open("linkedin.list","r")
    jobs = File.readlines()
    jobs_num = len(jobs)
    job_queue = Queue(jobs_num)
    for i in jobs:
        job_queue.put(i)
    #initiate the object of Downloading class
    for account in accounts:
        thread = DownloadJob(job_queue,process_id)
        threads.append(thread)
        process_id = process_id+1
    for i in threads:
        i.start()
    # wait until the input queue is empty   
    while not job_queue.empty():
        pass
    for i in threads:
        i.stop()  
