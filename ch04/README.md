### Chapter 4: Exposition (Detailed Summary)

Chapter 4 dives into how to expose metrics from applications in various programming languages and environments so that Prometheus can scrape them. This process is central to connecting Prometheus with the systems it monitors. The chapter also discusses advanced techniques like using Pushgateway, bridges, and different exposition formats.

#### **Python**:
- **Exposing Metrics**: In Python, you can use the `start_http_server()` method from the Prometheus Python client to expose metrics on an HTTP endpoint. This method spins up a basic web server that serves metrics under `/metrics`.
- **WSGI and Twisted**: For more advanced use cases, like web applications, WSGI can integrate metrics exposition into existing web servers. For asynchronous applications, Twisted also supports exposing metrics.
- **MultiProcessing**: In cases where Python applications use multiple processes (due to the Global Interpreter Lock or for parallel tasks), a **multi-process mode** is necessary. Each process writes its metrics to a temporary file, which Prometheus then aggregates during scraping.

#### **Go**:
- **Exposing Metrics**: In Go, exposing metrics is typically done via an HTTP handler integrated into the application. The Go client library makes this simple by providing an `http.Handle` function that automatically serves metrics at `/metrics`.
- Go's strong concurrency model makes it naturally fit for collecting and serving metrics efficiently, and it's widely used in Prometheus itself and other cloud-native projects.

#### **Java**:
- **Exposing Metrics**: Java developers can use `simpleclient_servlet` to expose metrics through servlet-based applications. This library integrates with Java’s web infrastructure and can be deployed on servers like Jetty or Tomcat.
- **Integration with Servlet**: Java servlets can expose metrics to Prometheus, allowing for a seamless integration with existing enterprise-level applications. Using the Prometheus client, metrics are pushed to the `/metrics` path and made accessible via HTTP.

#### **PushGateway**:
- **Use Case**: The PushGateway is designed for short-lived batch jobs or cron jobs that cannot be scraped continuously. Batch jobs push their metrics to the PushGateway, and Prometheus scrapes these from the gateway.
- **Push Method**: Rather than relying on Prometheus to scrape the batch job directly, the job sends its metrics (often just before termination) to the PushGateway. This ensures the metrics are not missed even if the job completes quickly.
- **Key Consideration**: PushGateway should not be overused for long-running services, as it goes against the pull-based model of Prometheus.

#### **Bridges**:
- **Metrics Conversion**: Bridges convert metrics from non-Prometheus monitoring systems to the Prometheus exposition format. They act as intermediaries, translating proprietary or different formats into something Prometheus can understand and scrape.
- **Examples**: Examples of bridges include tools that convert metrics from systems like StatsD, JMX, or SNMP into Prometheus-readable formats. They provide backward compatibility for systems not natively instrumented for Prometheus.

#### **Parsers**:
- **Handling Exposed Metrics**: Parsers help interpret the exposed metrics into the Prometheus format. They are crucial when working with custom metrics formats or ensuring that metrics follow the standards required by Prometheus.
- **Text and OpenMetrics Parsing**: Prometheus supports parsing metrics in both the traditional text format and the newer OpenMetrics format.

#### **Text Exposition Formats**:
- **Traditional Text Format**: The original Prometheus exposition format uses plain text. Each metric consists of key-value pairs and can be easily generated by libraries across different languages. This format allows the inclusion of labels, timestamps, and other metadata.
- **Metric Types**: The text format supports various metric types such as counters, gauges, histograms, and summaries. Labels help contextualize the metrics, while timestamps provide historical data points.

#### **OpenMetrics**:
- **Introduction**: OpenMetrics is a newer format developed from the Prometheus text exposition format to create a more universal and standardized way to expose metrics.
- **Enhanced Features**: OpenMetrics adds more consistency, ensuring interoperability between different monitoring systems. It includes standardized labels and additional metadata to make the metrics more versatile and useful across various tools.
- **Future Use**: OpenMetrics is expected to become the default format for Prometheus in the future, as it provides a more robust way to expose and manage metrics across multiple systems.

---

This chapter emphasizes the importance of choosing the correct exposition method for your environment and understanding how Prometheus gathers data via HTTP endpoints.