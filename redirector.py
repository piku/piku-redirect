#!/usr/bin/env python3
# https://stackoverflow.com/a/47084250/2131094

import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

port = os.environ.get("PORT", None)
url = os.environ.get("REDIRECT_URL", None)

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', url + self.path[1:])
       self.end_headers()

print("Starting redirector HTTPServer.")
print("Server params:", url, port)

if not (url and port):
    print("PORT or REDIRECT_URL not set!")
    sys.exit(1)
else:
    HTTPServer(("127.0.0.1", int(port)), Redirect).serve_forever()
