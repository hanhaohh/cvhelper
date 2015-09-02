import requests
from BeautifulSoup import BeautifulSoup
import re
import random
import time
# term = raw_inpu

class Linkedin (object):
	def __init__(self,account='',password='',ip = ''):
		if account == "" or password == "" : raise ValueError("please enter your account")
		self._account = account 
		self._password = password
		self._session = requests.session()
		self._ip = ip 

	@property
	def account(self):
	    return self._account
	@account.setter
	def account(self,value):
		if value == "":
			raise ValueError("account could not be empty")
		else:
			_account = value
	
	@property
	def password(self):
	    return self._password
	@password.setter
	def password(self,value):
		if value == "":
			print "error"
			raise ValueError("password could not be empty")
		_password = value

	@property
	def session(self):
	    return self._session

	#Linkedin randomly generate some kind of code in the html page for each login, you have submit the 
	#code along you login action. 
	def get_credential(self):
		r = self.session.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')
		soup = BeautifulSoup(r.text)
		loginCsrfParam = soup.find('input', id = 'loginCsrfParam-login')['value']
		csrfToken = soup.find('input', id = 'csrfToken-login')['value']
		sourceAlias = soup.find('input', id = 'sourceAlias-login')['value']
		payload = {
		'session_key': 'sxhanhao@gmail.com',
		'session_password': 'hanhaohh',
		'loginCsrfParam' : loginCsrfParam,
		'csrfToken' : csrfToken,
		'sourceAlias' : sourceAlias 
		}
		return payload
	#login the Linkedin with the cookies and temprory session in the Session. 
	def login(self):
		self.session.post('https://www.linkedin.com/uas/login-submit', data=self.get_credential())

	def crawl(self):
		term = "data"
		self.login()
		format1 = re.compile(r'link_nprofile_view_3"\:"[\\\w\d\s\:\/\=\?\.\$\&\%]*')
		for i in range(1,400,1):
		    page = "https://www.linkedin.com/vsearch/p?type=people&keywords="+term+"&openFacets=N,G,CC&pt=people&orig=FCTD&page_num="+str(i)
		    soup1 = BeautifulSoup(self.session.get(page).text.encode("utf-8"))
		    list1 = str(soup1.find('div',{"id":"srp_main_"}))
		    time.sleep(random.randint(6,12))
		    if list1.find("link_nprofile_view_3"):
		        contacts = format1.findall(list1)  
		        print contacts
		        for j in contacts:
		        	#get rid of the \u002d, it is "-" in unicode
		        	j = j.replace("\u002d","-")
		        	url= j.split('\"') [2]
		        	print "I am crawlling "+url
		        	time.sleep(random.randint(6,12))
		        	html = self.session.get(url)

a = Linkedin("sxhanhao@gmail.com","hanhaohh")
a.crawl()
