import requests
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
r = requests.get('http://api.theysaidso.com/qod.json')
Quote=r.json()

text=Quote["contents"]["quotes"][0]["quote"]
# text= Quote["success"]["total"]
for i in range(1,2):
    sendmessage("Quote of The Day",text)
sleep(0.5)