import scrapy

# 人物链接
class PersonUrlItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
