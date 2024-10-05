**Chapter 14: Aggregation Operators** based on common usage in PromQL.

### **1. Grouping: `without`, `by`**

PromQL allows you to aggregate data across multiple time series, often using **grouping modifiers** like `by` and `without`.

- **`by`**:
  The `by` clause groups time series by the specified labels. It keeps the listed labels intact and aggregates across the rest.
  
  - **Example (by)**:
    ```promql
    sum by (instance) (rate(http_requests_total[5m]))
    ```
    This query sums the HTTP request rates, grouped by the `instance` label. The result shows the rate of HTTP requests per instance.

- **`without`**:
  The `without` clause removes specific labels during aggregation, which means the aggregation is performed across the series that differ only by the removed labels.
  
  - **Example (without)**:
    ```promql
    sum without (instance, job, mode, cpu) (node_cpu_seconds_total)
    ```
    This sums the CPU time across all instances and jobs, ignoring differences in the `instance` and `job` labels. It gives the total CPU time across all nodes.

### **2. Operators**:

#### **`sum`**:
  - **Description**: Calculates the sum of all elements.
  - **Example**:
    ```promql
    sum(rate(http_requests_total[5m]))
    sum without(code, handler, instance, job) (rate(prometheus_http_requests_total[5m]))
    ```
    This query calculates the total rate of HTTP requests across all instances.

#### **`count`**:
  - **Description**: Returns the number of time series that match the query.
  - **Example**:
    ```promql
    count(prometheus_http_requests_total{code="200"})
    ```
    This query returns the number of time series where HTTP requests returned status code 500.

#### **`avg`**:
  - **Description**: Calculates the average value of time series.
  - **Example**:
    ```promql
    avg by (instance) (rate(node_cpu_seconds_total[5m]))
    ```
    This query calculates the average CPU usage rate per instance.

#### **`group`**:
  - **Description**: Groups the time series but doesn’t perform numerical aggregation.
  - **Example**:
    ```promql
    group by (job) (rate(http_requests_total[5m]))
    group by (job) (rate(prometheus_http_requests_total[5m]))
    ```
    This query groups the request rates by `job`, without changing the time series values.

#### **`stddev` and `stdvar`**:
  - **Description**: `stddev` computes the standard deviation, and `stdvar` computes the variance.
  - **Example (stddev)**:
    ```promql
    stddev(rate(http_requests_total[5m]))
    stddev(rate(prometheus_http_requests_total[5m]))
    ```
    This computes the standard deviation of the HTTP request rates across all time series.
  
  - **Example (stdvar)**:
    ```promql
    stdvar(rate(http_requests_total[5m]))
    stdvar(rate(prometheus_http_requests_total[5m]))
    ```
    This calculates the variance of HTTP request rates.

#### **`min` and `max`**:
  - **Description**: Returns the minimum or maximum value of the time series.
  - **Example (min)**:
    ```promql
    min(rate(http_requests_total[5m]))
    ```
    This query returns the minimum rate of HTTP requests.

  - **Example (max)**:
    ```promql
    max(rate(http_requests_total[5m]))
    ```
    This query returns the maximum rate of HTTP requests.

#### **`topk` and `bottomk`**:
  - **Description**: `topk` returns the top `k` series with the highest values, while `bottomk` returns the `k` lowest values.
  - **Example (topk)**:
    ```promql
    topk(3, rate(http_requests_total[5m]))
    topk(10, rate(prometheus_http_requests_total[5m]))
    ```
    This query returns the top 3 instances with the highest HTTP request rates.

  - **Example (bottomk)**:
    ```promql
    bottomk(3, rate(http_requests_total[5m]))
    bottomk(10, rate(prometheus_http_requests_total[5m]))
    ```
    This query returns the 3 instances with the lowest HTTP request rates.

#### **`quantile`**:
  - **Description**: Returns a quantile (percentile) for the distribution of values.
  - **Example**:
    ```promql
    quantile(0.95, rate(http_request_duration_seconds[5m]))
    quantile(0.95, rate(http_request_duration_microseconds[5m]))
    ```
    This query returns the 95th percentile of HTTP request duration over the past 5 minutes.

#### **`count_values`**:
  - **Description**: Counts the occurrence of each value in the time series.
  - **Example**:
    ```promql
    count_values("status_code", http_requests_total)
    count_values("status_code", prometheus_http_requests_total)
    ```
    This query counts how many times each HTTP status code appeared in the `http_requests_total` metric.

### Summary:
Chapter 14 introduces **aggregation operators** in PromQL, which allow you to manipulate, summarize, and analyze metrics by grouping data with labels using `by` and `without`. It also covers various operators like `sum`, `count`, `avg`, `min`, `max`, `topk`, `quantile`, and others, providing a powerful way to query, group, and aggregate time-series data for performance and health monitoring.