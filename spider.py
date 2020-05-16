from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class spider():
    
    def __init__(self,host):
        self.host = host
        self.eHrefArray=[]
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.google.com')

    def search(self,search:str):
        searchBar = self.driver.find_element_by_name('q')
        searchBar.send_keys(search)
        searchBar.submit()

    def clickATagHasHref(self,urlString:str) -> bool:
        aTagList = self.driver.find_elements_by_tag_name('a')
        for a in aTagList:
            href = str(a.get_attribute('href'))
            print(href)
            if href.find(urlString) != -1:
                a.click()
                return True
        return False

    def getElementHasClass(self,className:str):
        self.elementList = self.driver.find_elements_by_class_name(className)
        
    def getElementHasClassLength(self,className:str) ->int:
        return len(self.driver.find_elements_by_class_name(className))

    def getPost(self,index):
        print('elementList len:'+str(len(self.elementList)))
        print('index:'+str(index))
        if(len(self.elementList) - 1 ) < index:
            return False
        
        e = self.elementList[index]
        return e

    def hasAlreadyClicked(self,e)->bool:
        href = str(e.get_attribute('href'))
        return (href in self.eHrefArray)

    def clickElement(self,e):
        self.driver.execute_script("arguments[0].click();", e)

        
    def toHomePage(self):
        self.driver.get('https://tg-mediaweb.com/')

    
    def nextPage(self) ->bool:
        aTagList = self.driver.find_elements_by_class_name('next')

        for a in aTagList:
            href = str(a.get_attribute('href'))
            if href.find(self.host) != -1:
                a.click()
                return True
        return False



    def scroll(self):
        for i in range(20):
            page = self.driver.find_element_by_tag_name('html')
            page.send_keys(Keys.DOWN)
            time.sleep(3)

    def close(self):
        self.driver.close()
    def quite(self):
        self.driver.quit()