# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import codecs
import json
from scrapy.exporters import JsonItemExporter


class Demo1Pipeline:

    # def __init__(self):
    #     self.file = open("cpu.json", 'wb')
    #     self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
    #     self.exporter.start_exporting()

    def process_item(self, item, spider):
        # self.exporter.export_item(item)
        return item
