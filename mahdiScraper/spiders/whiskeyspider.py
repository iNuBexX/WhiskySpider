import scrapy
from mahdiScraper.items import MahdiscraperItem
from scrapy.loader import ItemLoader

class WhiskeySpider(scrapy.Spider):
    name='whisky'
    start_urls= ['https://whiskeyshop.com.ua/en/15-single-malt-whisky']
    
    #this is not so simple for web sites with dynamic content 
    
    def parse(self, response):
        
        for products in response.css('div.product-desc'):   
            l = ItemLoader(item = MahdiscraperItem(),selector=products)  
            l.add_css('name','a')
            l.add_css('price','span')
            l.add_css('link','a::attr(href)')

            """  item['name']=products.css('a::text').get()
            item['price']=products.css('span::text').get().replace('₴','')
            item['link']=products.css('a').attrib['href']"""

            yield  l.load_item()
        next_page = response.css('a.next.js-search-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

