#!/usr/bin/env python3
# https://stackoverflow.com/a/47084250/2131094

import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', os.environ.get("REDIRECT_URL", "") + self.path[1:])
       self.end_headers()

print("Starting redirector HTTPServer.")
HTTPServer(("", int(os.environ.get("PORT", "8000"))), Redirect).serve_forever()
