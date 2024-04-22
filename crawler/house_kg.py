import httpx
from parsel import Selector


class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"


    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        self.page = response.text


    def get_title(self):
        html = Selector(self.page)
        title = html.css("title::text").get()
        return title
    

    def get_house_links(self):
        html = Selector(self.page)
        links = html.css(".listing a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links[:3]
        

if __name__ == "__main__":
    crawler = HouseCrawler()
    crawler.get_page()
    # print("Title", crawler.get_title())
    crawler.get_house_links()
