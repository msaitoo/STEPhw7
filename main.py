#!/usr/bin/env python
import json
import random
import webapp2
from nextmove import nextmove

class MainHandler(webapp2.RequestHandler):
    html = '''
        <!doctype html>
        <html lang = "en">
            <body>
            <hl> Paste JSON: </hl>
            <br>
                <form method = "post">
                    <textarea name = "JSON" rows="10" cols="50"></textarea>
                    <br>
                    <input name = "" type = "submit" value = "Submit">
                </form>
            </body>
        </html>
        '''
    def get(self):
        self.response.write(self.html)
    
    def post(self):
        self.board = json.loads(self.request.get("JSON"))
        valid = self.board["valid_moves"]
        move = nextmove(valid)
        self.response.out.write(move)
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
