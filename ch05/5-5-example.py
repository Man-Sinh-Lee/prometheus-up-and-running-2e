import http.server
from prometheus_client import start_http_server, Summary
import time
from functools import wraps

# Create a Summary metric to track request latency
REQUEST_LATENCY = Summary('http_requests_latency_seconds', 'Request latency in seconds',
                           labelnames=['method', 'path'])

# Decorator for measuring latency
def measure_latency(method_name):
    @wraps(method_name)
    def wrapper(self, *args, **kwargs):
        # Start timing
        start_time = time.time()
        # Call the actual method
        response = method_name(self, *args, **kwargs)
        # Stop timing and observe the latency
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(method=self.command, path=self.path).observe(latency)
        return response
    return wrapper

class MyHandler(http.server.BaseHTTPRequestHandler):
    
    @measure_latency
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        return '200'  # Returning status for metric

    @measure_latency
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World POST")
        return '200'  # Returning status for metric

if __name__ == "__main__":
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    # Start the HTTP server on the specified address and port
    server = http.server.HTTPServer(('192.168.1.111', 8080), MyHandler)
    print("Serving on port 8080...")
    server.serve_forever()
