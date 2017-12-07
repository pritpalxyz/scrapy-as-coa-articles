# -*- coding: utf-8 -*-
import scrapy, re
from bs4 import BeautifulSoup
from as_coa_crawler.items import AsCoaCrawlerItem

class AsCoaSpider(scrapy.Spider):
    name = "as_coa"
    allowed_domains = ["as-coa.org"]
    start_urls = ['http://www.as-coa.org/region/united-states/']

    # DECLARING CONSTRUCTOR FOR PRE - CALLING
    # XPATH DECLARING METHOD
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.DeclareXpath()

    # METHOD FOR REMOVING UNWANTED CHARACTER FROM STRING
    def parseText(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        return re.sub(" +|\n|\r|\t|\0|\x0b|\xa0",' ',soup.get_text()).strip()

    # METHOD FOR CONVERTING LIST OF STRING TO SIMPLE STRING AND FILTRING
    def filterStr(self, listOfStr):
        dummy_string = ""
        for string_to_filter in listOfStr:
            dummy_string = unicode("{0} {1}".format(dummy_string,string_to_filter))
        return self.parseText(dummy_string)

    # METHOD FOR DECLARING ALL XPATH VARIABLES THAT
    # WILL BE USED FOR PARSING VALUES FROM PAGE
    def DeclareXpath(self):
        self.LIST_OF_EVENTS_XPATH = "//h1[@class='internal-title event']/a/@href"
        self.TITLE_XPATH = "//h1[@class='page-title bc']/text()"
        self.ARTICLE_IMAGE_XPATH = "//div[@class='article-hero']/img/@src"
        self.ARTICLE_IMAGE_CAPTION_XPATH = "//div[@class='article-hero']/p/text()"
        self.ARTICLE_DATE_XPATH = "//div[@class='field-item even']//span[@class='date-display-single']/text()"
        self.ARTICLE_DESCRIPTION_XPATH = "//div[@class='field-item even']"
        self.RELATED_XPATH = "//p[@class='related-tags']/span/a/text()"
        self.NEXT_PAGE_XPATH = "//li[@class='pager-next']/a/@href"

    # METHOD FOR PARSING LIST OF EVENT FROM PAGE
    def parse(self, response):
        for href in response.xpath(self.LIST_OF_EVENTS_XPATH):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.ParseEventDeep)

        # CALLING NEXT PAGE FROM LIST OF ARTICLE PAGE
        # AND RECALL CURRENT METHOD AGAIN FOR PARSING
        # ALL AVAILABLE ARTICLES
        next_page = response.xpath(self.NEXT_PAGE_XPATH)
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url,callback=self.parse)

    # PARSING ARTICLE PAGE ALL VALUES
    # AND STORING PASSING INTO ITEMS CLASS
    def ParseEventDeep(self, response):
        item = AsCoaCrawlerItem()
        

        item['eventImage'] = response.xpath(self.ARTICLE_IMAGE_XPATH).extract()
        item['organization'] = ''
        item['title'] = response.xpath(self.TITLE_XPATH).extract()
        item['description'] = response.xpath(self.ARTICLE_DESCRIPTION_XPATH).extract()
        item['eventWebsite'] = 'as-coa.org'
        item['street'] = ''
        item['city'] = ''
        item['state'] = response.xpath(self.RELATED_XPATH).extract()
        item['zip'] = ''
        item['dateFrom'] = response.xpath(self.ARTICLE_DATE_XPATH).extract()
        item['startTime'] = ''
        item['In_group_id'] = ''
        item['ticketUrl'] = response.url


        yield item
