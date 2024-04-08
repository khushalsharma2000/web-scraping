import scrapy


class AllSpider(scrapy.Spider):
    name = "all"
    start_urls = [
        "https://www.hidubai.com/search?resource=localBusiness&q=public%20relations%20officer&place=All%20of%20Dubai"]
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
        'FEED_URI': 'Public_relations_officer_MOBILE_NUMBERS.csv',
    }

    def start_requests(self):
        # You can set 'n' to any desired value
        n = 443

        # Loop through values from 0 to n
        for page_number in range(n + 1):
            url = f"https://api.hidubai.com/local-businesses/search?lat=25.197965&lon=55.273985&page={page_number}&place=All+of+Dubai&q=public+relations+officer&size=80"
            yield scrapy.Request(
                url=url,
                callback=self.parse_json,
                headers=self.headers
            )

    def parse_json(self, response):
        try:
            data = response.json().get("_embedded", {}).get("localBusinesses", [])
            for business in data:
                yield {
                    "BusinessName": business.get("businessName", {}).get("en"),
                    "LandlineNumber": business.get("contactPhoneObj", {}).get("fullPhoneNumber"),
                    "MobileNumber": business.get("mobilePhone"),
                }
        except Exception as e:
            self.log(f"Error processing JSON response: {e}")

# import scrapy
#
# class AllSpider(scrapy.Spider):
#     name = "all"
#     start_urls = [
#         "https://www.hidubai.com/search?resource=localBusiness&q=car%20rentals&lat=25.197965&lon=55.273985&place=All%20of%20Dubai"]
#     headers = {
#         "Accept": "application/json",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
#         "Referer": "https://www.hidubai.com/",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-site",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     }
#     custom_settings = {
#         'FEED_FORMAT': 'csv',
#         'FEED_URI': 'Businesslist.csv',
#     }
#
#     def parse(self, response):
#         yield scrapy.Request(
#             url="https://api.hidubai.com/categories/macro-categories",
#             callback=self.parse_json,
#             headers=self.headers
#         )
#
#     def parse_json(self, response):
#         try:
#             # Print the raw response for debugging
#             print(response.body)
#
#             data = response.json().get("categories", [])  # Update the key to 'categories'
#             for category in data:
#                 yield {
#                     "CategoryName": category.get("name", {}).get("en"),
#                 }
#         except Exception as e:
#             self.log(f"Error processing JSON response: {e}")

#
# import scrapy
#
#
# class AllSpider(scrapy.Spider):
#     name = "all"
#     start_urls = [
#         "https://www.hidubai.com/search?resource=localBusiness&q=gold%20trading&lat=25.197965&lon=55.273985&place=All%20of%20Dubai#"]
#     headers = {
#         "Accept": "application/json",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
#         "Referer": "https://www.hidubai.com/",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-site",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     }
#     custom_settings = {
#         'FEED_FORMAT': 'csv',
#         'FEED_URI': 'GoldTrading.csv',
#     }
#
#     def parse(self, response):
#         yield scrapy.Request(
#             url="https://api.hidubai.com/local-businesses/search?lat=25.197965&lon=55.273985&page=60&place=All+of+Dubai&q=gold+trading&size=80",
#             callback=self.parse_json,
#             headers=self.headers
#         )
#
#     def parse_json(self, response):
#         try:
#             data = response.json().get("_embedded", {}).get("localBusinesses", [])
#             for business in data:
#                 yield {
#                     "BusinessName": business.get("businessName", {}).get("en"),
#                     "LandlineNumber": business.get("contactPhoneObj", {}).get("fullPhoneNumber"),
#                     "MobileNumber": business.get("mobilePhone"),
#                 }
#         except Exception as e:
#             self.log(f"Error processing JSON response: {e}")