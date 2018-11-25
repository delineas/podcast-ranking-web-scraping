#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ranker import Ranker
from storage import Storage
import datetime

now = datetime.datetime.now()

# Get https://www.ivoox.com/podcast-internet-tecnologia_sc_f445_1.html (3 pages of results)
podcasts = Ranker('internet-tecnologia',445,3).build()
Storage.save('storage/ranking_{0}-{1}-{2}.json'.format(now.year,now.strftime('%m'),now.strftime('%d')), podcasts)