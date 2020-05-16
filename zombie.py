from spider import spider
import time
host = '/tg-mediaweb.com'


spider = spider(host)
spider.toHomePage()

while True:
    postLength = spider.getElementHasClassLength('gum-block-post-img')
    for i in range(postLength):
        spider.getElementHasClass('gum-block-post-img')
        post = spider.getPost(i)
        if(post != False):
            spider.clickElement(post)
            time.sleep(2)
            spider.scroll()
            spider.driver.back()

        
    result = spider.nextPage()
    if(result == False):
        spider.toHomePage()
        time.sleep(2)


    



def stop():
    spider.quite()