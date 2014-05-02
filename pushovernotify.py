__author__ = 'paul'
import httplib
import urllib


class pushOver(object):
    """Test Class"""
    def __init__(self, message):
        self.message = message

    def notify(self):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        ##conn = httplib.HTTPSConnection("184.154.74.158:443")
        conn.request("POST", "/1/messages.json",
                 urllib.urlencode({
                     "token": "*****************************",
                     "user": "******************************",
                     "message": self.message,
                     "sound": "magic",
                 }), {"Content-type": "application/x-www-form-urlencoded"})
        conn.getresponse()


