import urllib.request 
import re
import scrapy
import requests
from os import getenv

groups = {'group1': 'group1', 'group2': 'group2', 'group3': 'group3'}
 
GROUP_URL = set(getenv('GROUP_URL', 'http://contoso.com/group/'))
ITEM_URL = set(getenv('ITEM_URL', 'http://contoso.com/item/'))
LINK = r"(.*?)"
LINK_RE = re.compile(LINK)

class mySpider(scrapy.Spider): 
    name = "my"
    
    def start_requests(self):
        urls = get_urls()              
        for url_key, url_value in urls.items():
            yield scrapy.Request(url=url_value, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = '%s.html' % page
        print(filename)

    def get_urls():
        urls = {}

        isLast = None
        found = 0

        for url_key, url_value in groups.items():
            x = 0
            
            while True:
                page_url = GROUP_URL + url_value + '/?page=' + "%d" % (x)

                resource = urllib.request.urlopen(page_url)

                html = resource.read().decode(resource.headers.get_content_charset())

                found_link = html.find('pager') #TODO: Add last page criterion

                isLast = (True if found_link == -1 else False)

                links = re.findall(LINK_RE, html)

                for link in links:               
                    if link[0] in urls:
                        print('Skip duplicate url') 
                    else:
                        urls[link[0]] = ITEM_URL % link[0]

                if isLast:
                    break

                x = x + 1

        return urls

def scrape():
    # TODO: Add business logic
