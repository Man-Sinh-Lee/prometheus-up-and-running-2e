#!/usr/bin/env python3

import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter('hello_worlds',
        'Hello Worlds requested.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('192.168.1.111', 8090), MyHandler)
    server.serve_forever()
