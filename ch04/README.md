### Chapter 4: Exposition (Summary)

In this chapter, **exposition** refers to the process of making metrics available to Prometheus so they can be scraped and used for monitoring. Prometheus supports exposition through HTTP, where metrics are typically exposed under the `/metrics` path.

#### Key Components of Exposition:

1. **Metrics Formats**: Prometheus uses two main formats for metrics exposition:
   - **Prometheus Text Format**: A human-readable format, easier to produce manually but generally handled by libraries for accuracy in details like escaping special characters.
   - **OpenMetrics**: A stricter format designed for better compatibility across tools, evolving from the Prometheus text format.

2. **Exposing Metrics in Various Languages**:
   - **Python**: The `start_http_server()` function is a simple way to expose metrics through an HTTP server in Python. More advanced integrations, such as with WSGI or frameworks like Twisted, allow combining metric exposition with existing web servers.
   - **Go**: Similarly, Go applications can expose metrics via an HTTP handler. The example demonstrates a simple HTTP server that exposes metrics at `/metrics`.
   - **Java**: Java developers can use libraries like `simpleclient_servlet` to expose metrics through a servlet. Integration with existing servers like Jetty is supported.

3. **Pushgateway for Batch Jobs**: 
   - **Pushgateway** is designed for short-lived, batch jobs that cannot be scraped continuously by Prometheus. Batch jobs push their metrics to the Pushgateway before exiting, and Prometheus scrapes these metrics from the gateway. This setup is ideal for jobs where knowing whether they completed is more important than tracking the specifics of when or where they ran.

4. **Multiprocess Mode**: In cases like Python's CPython runtime, where multi-threading is constrained by the Global Interpreter Lock (GIL), Prometheus uses a **multiprocess mode** to aggregate metrics from multiple processes. This ensures that metrics are combined properly, avoiding issues like counters seeming to go backward when only one process is scraped.

5. **Text Exposition Format**: 
   - The text format allows various metric types (e.g., counters, gauges, histograms) to be represented with key-value pairs, often including labels and timestamps for more precise data analysis.

6. **Prometheus Tools**: 
   - Prometheus includes tools like **Promtool** to check and validate metrics from a `/metrics` endpoint. This helps ensure compliance with format standards and avoid common errors in metrics exposition.

Chapter 4 emphasizes the importance of exposing metrics correctly, as this is the bridge between instrumentation and monitoring. The use of libraries and tools makes it easier to ensure that metrics are exposed in the right format for Prometheus to scrape.