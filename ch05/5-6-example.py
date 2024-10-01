import http.server
from functools import wraps
from prometheus_client import start_http_server, Counter

# Create a Counter metric
REQUESTS = Counter('http_requests_total', 'Total HTTP requests',
                   labelnames=['method', 'path', 'status'])

# Decorator for counting requests
def count_requests(method_name):
    @wraps(method_name)
    def wrapper(self, *args, **kwargs):
        # Call the actual method
        response = method_name(self, *args, **kwargs)
        # Increment the counter with relevant labels
        REQUESTS.labels(method=self.command, path=self.path, status=response).inc()
        return response
    return wrapper

class MyHandler(http.server.BaseHTTPRequestHandler):
    
    @count_requests
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        return '200'  # Returning status for metric

    @count_requests
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
