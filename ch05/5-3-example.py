import http.server
from prometheus_client import start_http_server, Counter

# Create a Counter metric with parent and child labels
REQUESTS = Counter('http_requests_total', 'Total HTTP requests',
                   labelnames=['method', 'path', 'status'])

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        status = '200'  # Assume successful response
        # Increment the counter with labels
        REQUESTS.labels(method=self.command, path=self.path, status=status).inc()
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

    def do_POST(self):
        status = '200'  # Assume successful response for demonstration
        REQUESTS.labels(method=self.command, path=self.path, status=status).inc()
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World POST")

if __name__ == "__main__":
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    # Start the HTTP server on the specified address and port
    server = http.server.HTTPServer(('192.168.1.111', 8080), MyHandler)
    print("Serving on port 8080...")
    server.serve_forever()
