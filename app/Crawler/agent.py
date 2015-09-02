import urllib2,re
import threading
def get_proxy_list():  
    ''''' 
    http://www.cnproxy.com/proxy1.html 
    http://www.cnproxy.com/proxy2.html 
    http://www.cnproxy.com/proxy3.html 
    '''  
    portdicts = {'z':"3",'m':"4",'a':"2",'l':"9",'f':"0",'b':"5",'i':"7",'w':"6",'x':"8",'c':"1"}  
    proxylist = []      
    p=re.compile(r'''''<tr><td>(.+?)<SCRIPT type=text/javascript>document.write":"\+(.+?)</SCRIPT></td><td>(.+?)</td><td>.+?</td><td>(.+?)</td></tr>''')  
    for i in range(1,4):  
        target = r'http://www.cnproxy.com/proxy%d.html' %i  
        req = urllib2.urlopen(target)  
        result =  req.read()  
        match = p.findall(result)  
        for row in match:  
            ip = row[0]  
            port =row[1]  
            port = map(lambda x:portdicts[x],port.split('+'))  
            port = ''.join(port)  
            agent = row[2]  
            addr = row[3].decode("cp936").encode("utf-8")  
            proxylist.append([ip,port,agent,addr])  
    return proxylist  
class ProxyCheck(threading.Thread):  
    def __init__(self,proxy):  
        threading.Thread.__init__(self)  
        self.proxy = proxy  
        self.timeout = 5  
        self.test_url ="http://www.baidu.com/"  
        self.test_str = "030173"  
                
    def run(self):  
        global checkedProxyList  
        cookies = urllib2.HTTPCookieProcessor()  
        proxy_handler = urllib2.ProxyHandler({"http" : r'http://%s:%s' %(proxy[0],proxy[1])})  
        opener = urllib2.build_opener(cookies,proxy_handler)  
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A537a Safari/419.3')]   
        urllib2.install_opener(opener)  
        starttime=time.time()  
        try:  
            req = urllib2.urlopen(self.test_url,timeout=self.timeout)  
            result = req.read()  
            timeused = time.time()-starttime  
            pos = result.find(self.test_str)       
            if pos > -1:  
                checkedProxyList.append((proxy[0],proxy[1],proxy[2],proxy[3],timeused))       
                print "%s:%s\t%s\t%s\t%s\n"%(proxy[0],proxy[1],proxy[2],proxy[3],timeused)  
        except Exception,e:  
            print e.message          
if __name__ == '__main__':
    proxylist = get_proxy_list()
    print proxylist
    checkedProxyList=[]
    for proxy in proxylist:
        t = ProxyCheck(proxy)
        t.start()