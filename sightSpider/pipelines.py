# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class SightspiderPipeline(object):
    def __init__(self):
        self.f = open('sights.csv', 'w', encoding='utf-8', newline='')
        self.fieldnames = ['sightLocation', 'sightName',
                           'coordinate', 'photoUrl', 'intro']
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close(self, spider):
        self.f.close()
