import requests
from bs4 import BeautifulSoup
import urllib.parse

class Crawler():

    def __init__(self,urlString) -> None:


        url = urllib.parse.urlparse(urlString)
        self.host = url.scheme + "://" + url.netloc
        self.path = url.path

        print(self.host)
        print(self.path)


        response = requests.get(urlString)
        print(response.text)

        if self.isAdoultOnly(response):
            agreeUrl = self.host + "/ask/over18"
            data = {
                'from':self.path,
                'yes':'yes'
            }
            response = requests.post(agreeUrl,data=data)
            
        
        self.html = BeautifulSoup(response.text,features="html.parser")

    def isAdoultOnly(self,response) -> bool:
        if response.text.find("我同意，我已年滿十八歲") != -1:
            print("isAdoultOnly")
            return True

        return False
        
    def getElement(self,className) -> list:
        # print(self.html.select(className))
        return self.html.select(className)
        


# crawler = Crawler("http://localhost:8000")
crawler = Crawler("https://www.ptt.cc/bbs/Gossiping/M.1622805850.A.A81.html")
elementList = crawler.getElement('.article-meta-value')

for i in range(len(elementList)):
    print(elementList[i].string)