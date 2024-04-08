# import scrapy
#
# class AllSpider(scrapy.Spider):
#     name = "all"
#     base_url = "https://www.hidubai.com/businesses/"
#     start_urls = ["https://www.hidubai.com/search?resource=localBusiness&q=gold%20trading&lat=25.197965&lon=55.273985&place=All%20of%20Dubai"]
#     api_url = "https://api.hidubai.com/local-businesses/search?lat=25.197965&lon=55.273985&page=1&place=All+of+Dubai&q=gold+trading&size=80"
#
#     headers = {
#         "Accept": "application/json",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
#         "Referer": "https://www.hidubai.com/",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-site",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     }
#
#     custom_settings = {
#         'FEED_FORMAT': 'csv',
#         'FEED_URI': 'Urlforemails.csv',
#     }
#
#     def parse(self, response):
#         print(f"Processing main page: {response.url}")
#         yield scrapy.Request(
#             url=self.api_url,
#             callback=self.parse_json,
#             headers=self.headers
#         )
#
#     def parse_json(self, response):
#         try:
#             data = response.json().get("_embedded", {}).get("localBusinesses", [])
#             for business in data:
#                 friendly_url_name = business.get("friendlyUrlName")
#                 full_url = f"{self.base_url}{friendly_url_name}"
#
#
#
#                 yield {
#                     "FullURL": full_url,
#                 }
#         except Exception as e:
#             self.log(f"Error processing JSON response: {e}")

import scrapy

class AllSpider(scrapy.Spider):
    name = "all"
    base_url = "https://www.hidubai.com/businesses/"
    start_urls = ["https://www.hidubai.com/search?resource=localBusiness&q=gold%20trading&lat=25.197965&lon=55.273985&place=All%20of%20Dubai"]

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
        "Referer": "https://www.hidubai.com/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'Urlforemails.csv',
    }

    def start_requests(self):
        # You can set 'n' to any desired value
        max_pages = 25

        # Loop through values from 1 to n
        for page_number in range(9, max_pages):
            url = f"https://api.hidubai.com/local-businesses/search?lat=25.197965&lon=55.273985&page={page_number}&place=All+of+Dubai&q=gold+trading&size=80"
            yield scrapy.Request(
                url=url,
                callback=self.parse_json,
                headers=self.headers
            )

    def parse_json(self, response):
        try:
            data = response.json().get("_embedded", {}).get("localBusinesses", [])
            for business in data:
                friendly_url_name = business.get("friendlyUrlName")
                full_url = f"{self.base_url}{friendly_url_name}"

                yield {
                    "FullURL": full_url,
                }

        except Exception as e:
            self.log(f"Error processing JSON response: {e}")
