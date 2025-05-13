import time
from plyer import notification
while True:
    print("Please sip some water")
    notification.notify(title="Please dirnk some water",
                        message ="You need to derink some water")
    time.sleep(6)
