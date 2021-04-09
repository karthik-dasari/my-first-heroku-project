from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from whatsapp import send_message
sched = BlockingScheduler()
sched.add_job(send_message, 'interval', seconds=5)
sched.start()