import requests
from BeautifulSoup import BeautifulSoup
import re
import random
import time
Li = []
term = "data"
head = "www.linkedin.com"
s = requests.session()
r = s.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')
soup = BeautifulSoup(r.text)
loginCsrfParam = soup.find('input', id = 'loginCsrfParam-login')['value']
csrfToken = soup.find('input', id = 'csrfToken-login')['value']
sourceAlias = soup.find('input', id = 'sourceAlias-login')['value']
payload = {
'session_key': 'hanhaohh@126.com',
'session_password': 'hanhaohh123',
'loginCsrfParam' : loginCsrfParam,
'csrfToken' : csrfToken,
'sourceAlias' : sourceAlias
}
s.post('https://www.linkedin.com/uas/login-submit', data=payload)
File = open("test","w")
format1 = re.compile(r'link_viewJob_2"\:"[\w\d\s\:\/\;\=\?\.\$\&\%]*')
for i in range(1,2,1):
    print i
    page = "https://www.linkedin.com/vsearch/j?type=jobs&keywords="+term+"&orig=GLHD&rsid=2060029261441227217895&pageKey=voltron_job_search_internal_jsp&search=Search&locationType=I&countryCode=cn&openFacets=L,C&page_num="+str(i)+"&pt=jobs"
    # page = "https://www.linkedin.com/vsearch/p?type=people&keywords="+term+"&openFacets=N,G,CC&pt=people&orig=FCTD&page_num="+str(i)
    print page
    soup1 = BeautifulSoup(s.get(page).text.encode("utf-8"))
    list1 = str(soup1.find('div',{"id":"srp_main_"}))
    if list1.find("link_viewJob_2"):
        contacts = format1.findall(list1)  
        print len(contacts)
        for j in contacts:
            url= head+j.split('\"')[2].replace(";",'').replace("&amp","&")
            Li.append(url)
print (set(Li))