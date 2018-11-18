#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
from ivoox_scraper_client import IvooxScraperClient
from ranker import Ranker
from storage import Storage

# Get https://www.ivoox.com/podcast-internet-tecnologia_sc_f445_1.html (3 pages of results)
podcasts = Ranker('internet-tecnologia',445,3).build()
Storage.save('storage/ranking.json', podcasts)
