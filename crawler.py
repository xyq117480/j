from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
import unicodedata
import re
import traceback


class Crawler:

    def __init__(self, url):
        self.url = url
        self.queue = []
        self.res = set()
        self.email_regex = re.compile('([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})', re.IGNORECASE)

    def connect(self):
        driver = webdriver.Firefox()
        driver.get("http://" + self.url)
        html = driver.page_source
        soup = BeautifulSoup(html)
        for a in soup.find_all('a', href=True):
            m = re.search(self.email_regex, a["href"])
            if m:
                self.res.add(m.group(1)) 
            else:
                self.queue.append(a["href"])

        while self.queue:
            driver.get(self.queue.pop())
            html = driver.page_source
            soup = BeautifulSoup(html)
            for email in soup.find_all(text = self.email_regex):
                m = re.search(self.email_regex, email)
                if m:
                    self.res.add(m.group(1))

    def show(self):
        for item in self.res:
            print item

if __name__ == "__main__":
    import sys
    try:
        arg = sys.argv[1].lower()

        if arg.startswith("http://") and arg.startswith("https://"):
            print "Do not add http or https in your domain."
            sys.exit(0)
        
        crawler = Crawler(arg)
        crawler.connect()
        crawler.show()
    except Exception, e:
        traceback.print_exc()