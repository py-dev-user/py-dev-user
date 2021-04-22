from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import report


def send_report():
    scheduler = BackgroundScheduler()
    scheduler.add_job(report, 'interval', seconds=10)
    scheduler.start()
