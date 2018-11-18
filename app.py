from pprint import pprint
import json
from ivoox_scraper_client import IvooxScraperClient
from ranker import Ranker

# Get https://www.ivoox.com/podcast-internet-tecnologia_sc_f445_1.html (3 pages of results)
ranker = Ranker('internet-tecnologia',445,3)
podcasts = ranker.build()
print(json.dumps(podcasts))