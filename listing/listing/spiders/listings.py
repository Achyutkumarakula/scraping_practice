import scrapy
import pdb
import pandas as pd


def get_df(path):
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".xlsx"):
        df = pd.read_excel(path)
    elif path.endswith(".json"):
        df = read_json(path)
    else:
        raise Exception("The file is not an .csv,.xlsx or .json file")
    return df


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.aston.ac.uk']
    
    def start_requests(self):
        df=get_df("/home/achyut/scrapy_listing/listing/aston_courses.csv")
        records = df.to_dict("records")
        # print(records,"all records")
        for record in records:

            yield scrapy.Request(url=record['Course_link'],callback=self.parse,meta=record)

    def parse(self, response):
        
        item ={}
        name = response.meta['course_name']
        course_type = response.xpath("//div[@class='other_info']//div[@class='cr_type']/div/text()").get()
        course_format = response.xpath("///div[@class='cr_opinion']//div[@class='info']/text()").get()
        course_duration = response.xpath("//div[@class='cr_duration']//div[@class='info']/p/text()").get()
        ucas_code = response.xpath("//div[@class='cr_ucas']//div[@class='info']/p/text()").get()
        start_date =response.xpath("//div[@class='cr_start_date']//select//option/text()").get()
        
        item['name']=name
        item['course_type']=course_type
        item['course_format']=course_format
        item['course_duration']=course_duration
        item['ucas_code']=ucas_code
        item['start_date']=start_date
        # pdb.set_trace()

        yield item
