import scrapy
from pyquery import PyQuery as pq
from wiki_spider.items.person_items import PersonUrlItem

class Wiki1985Spider(scrapy.Spider):
    name = 'wiki1985'
    allowed_domains = ['zh.wikipedia.org']
    start_urls = [
        'https://zh.wikipedia.org/wiki/Category:1970%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1971%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1972%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1973%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1974%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1975%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1976%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1977%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1978%E5%B9%B4%E5%87%BA%E7%94%9F',
        'https://zh.wikipedia.org/wiki/Category:1979%E5%B9%B4%E5%87%BA%E7%94%9F',
    ]

    def parse(self,response):
        soup = pq(response.text)
        hrefs = soup('.mw-category-columns .mw-category-group a')
        for href in hrefs:
            url = href.attrib['href']
            item = PersonUrlItem()
            item['url'] = url
            item['name'] = href.text.strip()
            yield item
        # 下一页
        next_page = soup('#mw-pages a[href^="/w/"]:last-child')
        if next_page:
            url = next_page.attr("href")
            if url:
                # 根据完整的路径访问
                yield scrapy.Request(response.urljoin(url), callback=self.parse)