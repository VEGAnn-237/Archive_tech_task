import scrapper
import json


start_url = 'https://scrapeme.live/shop/'
json_dump = scrapper.scrape_all_pages(start_url)

result_json_file = open("result.json", "w")
result_json_file.write(json_dump)
result_json_file.close()