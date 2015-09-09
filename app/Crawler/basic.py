import os 
from BeautifulSoup import BeautifulSoup
from nltk.stem.snowball import SnowballStemmer
import re, string
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
    if top != None:
        title = top.find("h1",{"class":"title"}).text if top.find("h1",{"class":"title"}) else ''
        company = top.find("a",{"class":"company"}).text if top.find("a",{"class":"company"}) else ''
        location = top.find("span",{"itemprop":"jobLocation"}).text if top.find("span",{"itemprop":"jobLocation"}) else ''
    else :
        title = ""
        company = ""
        location = ""
    
    row = [title,company,location,plain_text]
    string =  "\t\t".join(row).encode("utf-8")
    try:
        with open(filename, 'w') as f:
            f.write(string)
    except :
        pass
    f.close()

def word_tokenize(text):
    try:
        return text.split("\t\t")[3].split(" ")
    except:
        return ""
def stem(word):
    try:
        stemmer = SnowballStemmer("english").stem
        return stemmer(word)
    except:
        return ""
 
def clean_html(html):
    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()
    raise NotImplementedError ("To remove HTML markup, use BeautifulSoup's get_text() function")
def remove_punc(text):
    for c in string.punctuation:
        text= text.replace(c,"")
    return text
