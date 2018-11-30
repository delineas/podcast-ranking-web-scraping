from apscheduler.schedulers.blocking import BlockingScheduler
from ranker import Ranker
from storage import Storage
import datetime

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon', hour=12)
def scheduled_job():
    """
        This job is run every monday at 12.
    """
    now = datetime.datetime.now()
    podcasts = Ranker('internet-tecnologia',445,5).build()
    Storage.save('storage/ranking_{0}-{1}-{2}.json'.format(now.year,now.strftime('%m'),now.strftime('%d')), podcasts)

scheduler.start()