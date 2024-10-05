Here's a detailed summary of **Chapter 13: Introduction to PromQL**, covering the requested sections:

### **1. Aggregation Basics:**
PromQL provides aggregation operators to work with various metric types like gauges, counters, summaries, and histograms.

#### **Gauge**
A gauge is a metric that represents a value at a specific point in time and can go up or down (e.g., memory usage, CPU utilization).

- **Example Query (Gauge)**: 
  ```promql
  avg(node_memory_MemFree_bytes)
  ```
  This query calculates the average free memory across all nodes.

#### **Counter**
A counter is a metric that only increases (or resets) over time (e.g., number of HTTP requests).

- **Example Query (Counter)**:
  ```promql
  rate(http_requests_total[5m])
  ```
  This query returns the per-second rate of HTTP requests over the last 5 minutes, which is commonly used for monitoring throughput.

#### **Summary**
Summaries provide aggregate data about the distribution of a set of values, such as request latencies. Summaries track `_count`, `_sum`, and quantiles.

- **Example Query (Summary)**:
  ```promql
  rate(http_request_duration_seconds_sum[5m]) / rate(http_request_duration_seconds_count[5m])
  ```
  This query calculates the average request duration by dividing the sum of request durations by the count of requests over the last 5 minutes.

#### **Histogram**
Histograms record observations in buckets, with metrics like `_bucket`, `_sum`, and `_count`. They are often used for measuring latencies.

- **Example Query (Histogram)**:
  ```promql
  histogram_quantile(0.95, rate(prometheus_http_request_duration_seconds_bucket[5m]))
  ```
  This query calculates the 95th percentile of request durations over the past 5 minutes, which is a common metric to track latencies.

### **2. Selectors**
Selectors allow you to filter and slice metrics based on labels and other parameters.

#### **Matchers**
Matchers filter time series based on label values using `=`, `!=`, `=~`, or `!~`.

- **Example Query (Matchers)**:
  ```promql
  http_requests_total{method="get", code="200"}
  ```
  This query retrieves the total number of successful `GET` requests.

#### **Instant Vector**
An instant vector query returns the current value of a time series.

- **Example Query (Instant Vector)**:
  ```promql
  node_cpu_seconds_total{mode="idle"}
  ```
  This query retrieves the most recent value of CPU time spent idle.

#### **Range Vector**
Range vectors return time series data over a specific range of time.

- **Example Query (Range Vector)**:
  ```promql
  rate(node_network_receive_bytes_total[1m])
  ```
  This query calculates the rate of bytes received over the network in the last minute.

#### **Subqueries**
Subqueries allow you to apply functions over a range within another query.

- **Example Query (Subqueries)**:
  ```promql
  avg_over_time(rate(http_requests_total[5m])[30m:])
  ```
  This query calculates the average rate of HTTP requests over 30-minute intervals.

#### **Offset**
The `offset` modifier shifts a time series back in time.

- **Example Query (Offset)**:
  ```promql
  node_cpu_seconds_total{mode="idle"} offset 1h
  ```
  This query retrieves the idle CPU time as it was 1 hour ago.

#### **At Modifier**
The `@` modifier allows you to query data from a specific point in time, rather than the current time.

- **Example Query (At Modifier)**: (date -d "1 hour ago" +%s)
  ```promql
  http_requests_total @ 1633024800
  ```
  This query retrieves the value of `http_requests_total` at the Unix timestamp `1633024800`.

### **3. HTTP API**
Prometheus provides two main endpoints to execute PromQL queries via the HTTP API.

#### **Query (`/api/v1/query`)**
This endpoint executes an instant query at a specific point in time.

- **Example Query (HTTP API - `query`)**:
  ```bash
  curl 'http://localhost:9090/api/v1/query?query=node_memory_MemFree_bytes'
  ```
  This returns the most recent free memory value for each node.

#### **Query Range (`/api/v1/query_range`)**
This endpoint retrieves metrics over a range of time, returning a series of values at specific intervals.

- **Example Query (HTTP API - `query_range`)**:
  ```bash
  curl 'http://localhost:9090/api/v1/query_range?query=rate(http_requests_total[5m])&start=1633010400&end=1633024800&step=60'
  ```
  This retrieves the rate of HTTP requests over 5-minute intervals between the specified start and end times, with a step size of 60 seconds.

---

This summary covers the main concepts and provides example queries for **aggregation basics**, **selectors**, and the **HTTP API** in Prometheus, illustrating how PromQL works with different metric types and data selection methods.