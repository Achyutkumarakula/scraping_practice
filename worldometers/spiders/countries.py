from urllib import response
import scrapy
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # countries = response.xpath("//td/a")
        # for country in countries:
        #     name = country.xpath(".//text()").get()
        #     link = country.xpath(".//@href").get()

            #absolute_url = f"https://www.worldometers.info{link}"
            #absolute_url = response.urljoin(link)

            yield response.follow(url="https://www.worldometers.info/world-population/united-arab-emirates-population/",callback=self.parse_country,meta={'country_name':'United_Arab_Emirates'})

    def parse_country(self,response):
        # logging.warning(response.status)
        # open_in_browser(response)
        # inspect_response(response,self)
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield{
                'country_name':name,
                'year':year,
                'population':population
            }