from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import report


def send_report():
    scheduler = BackgroundScheduler()
    scheduler.add_job(report, 'interval', hours=168)
    scheduler.start()
