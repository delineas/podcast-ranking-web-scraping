from pprint import pprint
import json
from ivoox_scraper_client import IvooxScraperClient
from ranker import Ranker

ranker = Ranker('internet-tecnologia',445,3)
podcasts = ranker.build()
print(json.dumps(podcasts))