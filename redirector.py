#!/usr/bin/env python3
# https://stackoverflow.com/a/47084250/2131094

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 2:
    print("""Usage: {} <port_number> <base_url>""".format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[2] + self.path[1:])
       self.end_headers()

print("Starting redirector HTTPServer.")
HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
