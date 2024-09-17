#!/usr/bin/env python3

import http.server
from prometheus_client import start_http_server
from prometheus_client import Summary

LATENCY = Summary('hello_world_latency_seconds',
        'Time for a request Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('192.168.1.111', 8090), MyHandler)
    server.serve_forever()
