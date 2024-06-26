from wiki_spider.service.person_service import PersonUrlService,PersonUrl
from wiki_spider.items.person_items import PersonUrlItem


class MysqlPipeline(object):
    def __init__(self):
        self.personUrlService = PersonUrlService()

    def process_item(self, item, spider):
        if type(item) == PersonUrlItem:
            record = PersonUrl(**item)
            self.personUrlService.add(record)
        pass

    @classmethod
    def from_settings(cls, settings):
        return cls()

if __name__ == '__main__':
    pass