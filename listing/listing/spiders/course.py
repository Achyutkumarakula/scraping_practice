import scrapy

class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['www.aston.ac.uk']
    start_urls = ['https://www.aston.ac.uk/courses-atoz']

    def parse(self, response):
        blocks = response.xpath("//div[@class='view-content']//div[@class='views-row']")
        for block in blocks:
            name=block.xpath(".//div[@class='title']/text()").get()
            link=block.xpath(".//@href").get()

            absolute_url = response.urljoin(link)
            meta={}
            meta['name']=name
            yield scrapy.Request(absolute_url,callback=self.course_details,meta={'course_name':name})
            
    def course_details(self,response):

        name=response.request.meta['course_name']
        course_type = response.xpath("//div[@class='other_info']//div[@class='cr_type']/div/text()").get()
        course_format = response.xpath("///div[@class='cr_opinion']//div[@class='info']/text()").get()
        course_duration = response.xpath("//div[@class='cr_duration']//div[@class='info']/p/text()").get()
        ucas_code = response.xpath("//div[@class='cr_ucas']//div[@class='info']/p/text()").get()
        start_date =response.xpath("//div[@class='cr_start_date']//select//option/text()").get()
        yield{
            'course_name':name,
            'course_type':course_type,
            'course_format':course_format,
            'course_duration':course_duration,
            'ucas_code':ucas_code,
            'start_date':start_date
        }