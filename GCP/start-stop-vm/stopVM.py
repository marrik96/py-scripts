import webapp2
import urllib2
import mimetypes

class MonthCronPage(webapp2.RequestHandler):
    def get(self):
        response = urllib2.urlopen('https://asia-northeast1-gcp-test-178407.cloudfunctions.net/stopVM')
        app = webapp2.WSGIApplication([('/stop', MonthCronPage),], debug=True)