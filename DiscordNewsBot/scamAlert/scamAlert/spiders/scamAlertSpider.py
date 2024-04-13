import scrapy
from pathlib import Path
from scamAlert.items import ScamNewsItem
from datetime import datetime

class ScamalertspiderSpider(scrapy.Spider):
    name = "scamAlertSpider"
    allowed_domains = ["www.scamalert.sg"]

    def start_requests(self):
        base_url = 'https://www.scamalert.sg/news/GetNewsListAjax/?'
        current_year = datetime.now().year
        current_month = datetime.now().month
        for year in range(2016, current_year):
            for month in range(1, 13):
                url = f'{base_url}scamType=&year={year}&month={month}&page=1&sortBy=Latest'
                yield scrapy.Request(url, self.parse)
        for month in range(1, current_month + 1):
            url = f'{base_url}scamType=&year={current_year}&month={month}&page=1&sortBy=Latest'
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        newsItem = []
        for each in response.xpath("//div[@class='col-md-4']"):
            title = (each.xpath("div/div/h4/a/text()").extract())
            time = (each.xpath("div/div/div/text()").extract())
            url = (each.xpath("div/div/h4/a/@href").extract())
            item = ScamNewsItem()
            date_object = datetime.strptime(time[0], '%d %b %Y')
            item["title"] = title[0]
            item["time"] = date_object
            item["url"] = url[0]
            item["type"] = ''
            item["isPosted"] = False
            item["isValid"] = True
            item["author"] = ''
            item["content"] = ''
            yield item
            print(title)
            print(time)
            print(url)
