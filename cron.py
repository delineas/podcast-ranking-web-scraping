from apscheduler.schedulers.blocking import BlockingScheduler
from ranker import Ranker
from storage import Storage
import datetime

scheduler = BlockingScheduler()

# , day_of_week='mon', hour=12
@scheduler.scheduled_job('cron', minute=0) 
def scheduled_job():
    """
        This job is run every monday at 12.
    """
    now = datetime.datetime.now()
    podcasts = Ranker('internet-tecnologia',445,5).build()
    Storage.save('storage/ranking_{0}-{1}-{2}.json'.format(now.year,now.strftime('%m'),now.strftime('%d')), podcasts)

scheduler.start()