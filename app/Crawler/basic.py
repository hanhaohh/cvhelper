import os 
from BeautifulSoup import BeautifulSoup

def save(data, filename, dir=None):
    try:
        with open(filename, 'a') as f:
            for i in data:
                f.write(i+"\n")
    except FileNotFoundError as e:
        dir = os.path.dirname(filename)
        os.makedirs(dir)
        with open(filename, 'wb') as f:
            f.write(data)
    f.close()
    return filename

def save_data(data,filename):
    
    soup = BeautifulSoup(data)
    content = soup.findAll('div',{"class":"rich-text","itemprop":"description"})
    content = [str(i) for i in content]
    plain_text = "".join(list(content)).decode("utf-8")
    top = soup.find("div",{"class":"top-row"})
    title = top.find("h1",{"class":"title"}).text if top.find("h1",{"class":"title"}) else ''
    
    company = top.find("a",{"class":"company"}).text if top.find("a",{"class":"company"}) else ''
    location = top.find("span",{"itemprop":"jobLocation"}).text if top.find("span",{"itemprop":"jobLocation"}) else ''
    row = [title,company,location,plain_text]
    string =  "\t\t".join(row).encode("utf-8")
    try:
        with open(filename, 'w') as f:
            f.write(string)
    except :
        pass
    f.close()
