In Prometheus, a **registry** is a central repository or collection of metrics that are collected and exposed by a Prometheus client. It is used to manage and aggregate metrics, particularly when dealing with complex setups or multi-process environments. Here’s a breakdown of what a registry is and its role:

### Key Concepts of a Registry

1. **CollectorRegistry**:
   - **Purpose**: The `CollectorRegistry` class in Prometheus Client Libraries (e.g., Python, Go) acts as a container for all the metrics collectors.
   - **Function**: It holds all the `Collector` instances (e.g., `Counter`, `Gauge`, `Histogram`) and manages their registration and aggregation.

2. **Usage**:
   - **Default Registry**: By default, Prometheus Client Libraries use a global or default registry. This means that if you do not explicitly create a `CollectorRegistry`, metrics will be registered with the default one.
   - **Custom Registries**: You can create custom `CollectorRegistry` instances if you need to manage different sets of metrics separately. This is useful in multi-process setups or complex applications where you need fine-grained control over which metrics are exposed and how they are aggregated.

3. **MultiProcessCollector**:
   - **Role**: In multi-process setups (e.g., when using a process manager like Gunicorn), you may use `MultiProcessCollector` to aggregate metrics collected by multiple processes into a single registry.
   - **Function**: It collects metrics from all processes and aggregates them according to the specified mode (e.g., `livesum`, `sum`, `avg`, etc.).

### Example Usage

Here’s an example of how a `CollectorRegistry` might be used in Python with the Prometheus Client library:

```python
from prometheus_client import CollectorRegistry, Counter, make_wsgi_app
from prometheus_client.exposition import generate_latest

# Create a custom registry
registry = CollectorRegistry()

# Define metrics and register them with the custom registry
REQUESTS = Counter('http_requests_total', 'HTTP requests', registry=registry)
ERRORS = Counter('http_errors_total', 'HTTP errors', registry=registry)

# Define a WSGI app that serves metrics from the custom registry
def app(environ, start_response):
    if environ['PATH_INFO'] == '/metrics':
        output = generate_latest(registry)
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [output]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello World']

# Use the custom app to serve metrics
from wsgiref.simple_server import make_server
httpd = make_server('', 8000, app)
httpd.serve_forever()
```

### Summary

- **Registry**: A central place to manage and aggregate metrics.
- **CollectorRegistry**: Manages individual metric collectors and their registration.
- **MultiProcessCollector**: Aggregates metrics from multiple processes into a single registry.

Using a `CollectorRegistry` allows for flexibility in managing metrics, especially in environments with multiple processes or complex metrics setups.