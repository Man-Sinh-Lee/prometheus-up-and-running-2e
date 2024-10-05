**Chapter 16: Functions** in PromQL, covering the requested sections.

### **1. Changing Type: `vector`, `scalar`**

PromQL provides functions to convert between different types of time series, specifically between vectors and scalars.

- **`vector()`**: Converts a scalar into a vector.
  - **Example**:
    ```promql
    vector(5)
    ```
    This returns a vector with the value 5 for all time series.

- **`scalar()`**: Converts a single element vector into a scalar.
  - **Example**:
    ```promql
    scalar(node_memory_MemFree_bytes)
    ```
    This returns the scalar value of free memory.

---

### **2. Math Functions**

PromQL includes various mathematical functions to manipulate time series data.

- **`abs()`**: Returns the absolute value.
  - **Example**:
    ```promql
    abs(-node_cpu_seconds_total)
    ```

- **`ln()`**: Natural logarithm.
  - **Example**:
    ```promql
    ln(node_memory_MemTotal_bytes)
    ```

- **`log2()`**: Base-2 logarithm.
  - **Example**:
    ```promql
    log2(node_memory_MemFree_bytes)
    ```

- **`log10()`**: Base-10 logarithm.
  - **Example**:
    ```promql
    log10(node_memory_MemFree_bytes)
    ```

- **`exp()`**: Exponential function.
  - **Example**:
    ```promql
    exp(node_cpu_seconds_total)
    ```

- **`sqrt()`**: Square root.
  - **Example**:
    ```promql
    sqrt(node_cpu_seconds_total)
    ```

- **`ceil()` and `floor()`**: Ceil rounds up, floor rounds down.
  - **Example**:
    ```promql
    ceil(rate(node_cpu_seconds_total[5m]))
    floor(rate(node_cpu_seconds_total[5m]))
    ```

- **`round()`**: Rounds to the nearest integer or a given precision.
  - **Example**:
    ```promql
    round(node_cpu_seconds_total, 2)
    ```

- **`clamp()`, `clamp_max()`, `clamp_min()`**: Restrict values within a range.
  - **Example**:
    ```promql
    clamp_min(node_memory_MemFree_bytes, 1024)
    ```

- **`sgn()`**: Returns the sign of a value.
  - **Example**:
    ```promql
    sgn(node_cpu_seconds_total)
    ```

- **Trigonometric functions**: Includes `sin()`, `cos()`, `tan()`, etc.
  - **Example**:
    ```promql
    sin(time())
    ```

---

### **3. Time and Date Functions**

PromQL includes functions to extract components of time.

- **`time()`**: Returns the Unix timestamp.
  - **Example**:
    ```promql
    time()
    ```

- **`minute()`, `hour()`, `day_of_week()`, etc.**: Extracts parts of the current time.
  - **Example**:
    ```promql
    day_of_week(time())
    ```

- **`timestamp()`**: Returns the timestamp of the last sample in a time series.
  - **Example**:
    ```promql
    timestamp(node_cpu_seconds_total)
    ```

---

### **4. Labels**

- **`label_replace()`**: Replaces the value of a label.
  - **Example**:
    ```promql
    label_replace(http_requests_total, "new_label", "$1", "status", "(.+)")
    ```

- **`label_join()`**: Joins multiple labels into a single label.
  - **Example**:
    ```promql
    label_join(http_requests_total, "all_labels", ",", "job", "instance")
    ```

---

### **5. Missing Series**

- **`absent()`**: Returns a series with value `1` if no series match the selector.
  - **Example**:
    ```promql
    absent(http_requests_total)
    ```

- **`absent_over_time()`**: Checks if there are no data points over a range of time.
  - **Example**:
    ```promql
    absent_over_time(http_requests_total[5m])
    ```

---

### **6. Sorting**

- **`sort()`**: Sorts values in ascending order.
  - **Example**:
    ```promql
    sort(rate(http_requests_total[5m]))
    ```

- **`sort_desc()`**: Sorts values in descending order.
  - **Example**:
    ```promql
    sort_desc(rate(http_requests_total[5m]))
    ```

---

### **7. Histograms**

- **`histogram_quantile()`**: Calculates a quantile (e.g., 95th percentile) from a histogram.
  - **Example**:
    ```promql
    histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
    ```

---

### **8. Counters**

- **`rate()`**: Calculates the per-second average rate of increase for a counter.
  - **Example**:
    ```promql
    rate(http_requests_total[5m])
    ```

- **`increase()`**: Calculates the total increase over a time range.
  - **Example**:
    ```promql
    increase(http_requests_total[1h])
    ```

- **`irate()`**: Instantaneous rate of increase between the two most recent samples.
  - **Example**:
    ```promql
    irate(http_requests_total[5m])
    ```

- **`resets()`**: Counts the number of times a counter resets.
  - **Example**:
    ```promql
    resets(http_requests_total[1h])
    ```

---

### **9. Changing Gauges**

- **`changes()`**: Counts the number of times a gauge changes over a range.
  - **Example**:
    ```promql
    changes(node_cpu_seconds_total[1h])
    ```

- **`deriv()`**: Computes the per-second derivative.
  - **Example**:
    ```promql
    deriv(node_cpu_seconds_total[5m])
    ```

- **`predict_linear()`**: Predicts the value of a time series at a future time based on its rate of change.
  - **Example**:
    ```promql
    predict_linear(node_cpu_seconds_total[5m], 3600)
    ```

- **`delta()`**: Calculates the difference between the first and last values in a range.
  - **Example**:
    ```promql
    delta(node_cpu_seconds_total[5m])
    ```

- **`idelta()`**: Calculates the difference between the last two samples in a range.
  - **Example**:
    ```promql
    idelta(node_cpu_seconds_total[5m])
    ```

- **`holt_winters()`**: Performs a Holt-Winters forecast.
  - **Example**:
    ```promql
    holt_winters(node_cpu_seconds_total[5m], 0.1, 0.2)
    ```

---

### **10. Aggregation Over Time**
In PromQL, **Aggregation Over Time** functions allow you to summarize, reduce, and analyze metrics over a specified time range. These functions are typically applied to **range vectors** and help in understanding trends, averages, and changes in system behavior over a period. Aggregation functions like `avg_over_time`, `sum_over_time`, `min_over_time`, and `max_over_time` help you understand trends and variations in your data over time. These functions are crucial for analyzing long-term behavior in metrics such as CPU usage, memory consumption, and network traffic, providing insights into system health and performance.

Here’s a breakdown of some common **Aggregation Over Time** functions with examples:

### **10.1 `avg_over_time`**
- **Description**: Returns the average value of the time series over a specified range.
  
- **Example**:
  ```promql
  avg_over_time(node_cpu_seconds_total[5m])
  ```
  This query calculates the average CPU usage over the last 5 minutes.

### **10.2 `sum_over_time`**
- **Description**: Returns the sum of the time series over the specified range.

- **Example**:
  ```promql
  sum_over_time(rate(http_requests_total[5m])[1h:])
  ```
  This query sums the rate of HTTP requests over each 1-hour window for the last 5 minutes.

### **10.3 `min_over_time`**
- **Description**: Returns the minimum value of the time series in the specified range.

- **Example**:
  ```promql
  min_over_time(node_memory_MemFree_bytes[10m])
  ```
  This query returns the minimum amount of free memory in the past 10 minutes.

### **10.4 `max_over_time`**
- **Description**: Returns the maximum value of the time series in the specified range.

- **Example**:
  ```promql
  max_over_time(node_memory_MemFree_bytes[10m])
  ```
  This query retrieves the maximum free memory in the last 10 minutes.

### **10.5 `count_over_time`**
- **Description**: Counts the number of values in the time series over the specified range.

- **Example**:
  ```promql
  count_over_time(node_network_receive_bytes_total[1h])
  ```
  This query counts how many samples have been collected for received network bytes over the past hour.

### **10.6 `quantile_over_time`**
- **Description**: Calculates the given quantile for the time series over a specified range.

- **Example**:
  ```promql
  quantile_over_time(0.95, http_request_duration_seconds[10m])
  ```
  This query calculates the 95th percentile of HTTP request durations over the past 10 minutes.

### **10.7 `stddev_over_time`**
- **Description**: Calculates the standard deviation of the time series over the given range.

- **Example**:
  ```promql
  stddev_over_time(node_memory_MemFree_bytes[1h])
  ```
  This query returns the standard deviation of free memory values over the last hour.

### **10.8 `stdvar_over_time`**
- **Description**: Calculates the variance of the time series over the given range.

- **Example**:
  ```promql
  stdvar_over_time(node_memory_MemFree_bytes[1h])
  ```
  This query returns the variance in free memory values over the past hour.