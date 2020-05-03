from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

keyWords = [
    '流線小巧',
    'Sony',
    ]

host = '/tg-mediaweb.com'

class spider():
    
    def __init__(self):
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

    def clickATagHasText(self) -> bool:
        for keyWord in keyWords:
            aTagList = self.driver.find_elements_by_partial_link_text(keyWord)
            for a in aTagList:
                innerHtml = str(a.get_attribute('innerHTML'))
                print(innerHtml)
                if innerHtml.find(keyWord) != -1:
                    a.click()
                    return True
        # 都沒有找到
        hasNext = self.nextPage()
        if(hasNext):
            return self.clickATagHasText()
        else:
            return False

    
    def nextPage(self) ->bool:
        aTagList = self.driver.find_elements_by_class_name('next')

        for a in aTagList:
            href = str(a.get_attribute('href'))
            if href.find(host) != -1:
                a.click()
                return True
        return False



    def scroll(self):
        for i in range(25):
            page = self.driver.find_element_by_tag_name('html')
            page.send_keys(Keys.DOWN)
            time.sleep(3)

    def close(self):
        self.driver.close()
    def quite(self):
        self.driver.quit()




spider = spider()
hasSearch = False
if hasSearch == False:
    spider.search('tg-mediaweb.com')
    time.sleep(2)
    hasSearch = spider.clickATagHasHref(host)
    if(hasSearch):
        time.sleep(2)
        hasText = spider.clickATagHasText()
        if hasText:
            spider.scroll()

    

spider.quite()



