**Chapter 17: Recording Rules** in PromQL, based on how recording rules are generally used in Prometheus.

### **1. Using Recording Rules**
Recording rules in Prometheus allow you to precompute queries and store the result as a new time series, improving performance by reducing the computational load during query execution. These precomputed time series are stored back into Prometheus, and you can query them just like any other metric.

#### **Example and Configuration**:
- A common use case is to store CPU usage metrics that are frequently queried:
  
  **Recording Rule**:
  ```yaml
  groups:
    - name: example
      rules:
        - record: instance:node_cpu_usage:rate5m
          expr: rate(node_cpu_seconds_total[5m])
  ```

  **Explanation**:
  - **`record`**: Defines the new time series name (`instance:node_cpu_usage:rate5m`).
  - **`expr`**: Specifies the expression to compute and store (`rate(node_cpu_seconds_total[5m])`).
  
  Prometheus will execute the query defined by `expr` regularly, store the result in `instance:node_cpu_usage:rate5m`, and allow it to be queried directly.

### **2. When to Use Recording Rules**
Recording rules are particularly useful in scenarios where queries are resource-intensive or frequently used. They also help reduce query complexity and improve performance.

#### **Reducing Cardinality**:
- Prometheus can generate high-cardinality data when there are many unique label combinations. Recording rules can pre-aggregate data to reduce this cardinality.
  
  **Example**:
  ```yaml
  record: job:node_cpu_usage:rate5m
  expr: sum without (cpu)(rate(node_cpu_seconds_total[5m]))
  ```
  This recording rule aggregates CPU usage across all cores for each job, reducing the number of unique time series Prometheus has to handle.

#### **Composing Range Vector Functions**:
- Complex queries that involve multiple range vector functions can be precomputed using recording rules to simplify future queries.

  **Example**:
  ```yaml
  record: job:node_cpu_usage:5m_avg
  expr: avg_over_time(instance:node_cpu_usage:rate5m[5m])
  ```
  This rule stores the 5-minute average CPU usage, allowing simpler queries that reference this precomputed data.

#### **Rules for APIs**:
- Recording rules can be useful when exposing precomputed data via APIs. This reduces the need to compute metrics dynamically when queried externally.

  **Example**:
  If a monitoring dashboard frequently requests the same aggregated metrics, recording rules can cache these metrics and speed up the API responses.

#### **How Not to Use Rules**:
- Don’t use recording rules for metrics that are rarely queried or when real-time computation is required. Overuse of recording rules can lead to unnecessary storage usage and increased complexity.

  **Bad Example**:
  ```yaml
  record: unnecessary_rule
  expr: rate(http_requests_total[1m])
  ```
  This rule computes HTTP request rates with a 1-minute window, which may not be useful for most queries that prefer a larger window.

### **3. Naming of Recording Rules**
Naming conventions are important for clarity and consistency, especially in large environments where multiple teams might be creating rules.

#### **Guidelines for Naming**:
- Use descriptive names that reflect the content and aggregation applied.
- Follow the convention `<scope>:<metric_name>:<aggregation_window>`. The scope often indicates the level of aggregation (e.g., `job`, `instance`), the metric name describes the original metric, and the aggregation window denotes the time range or function applied.

#### **Example**:
```yaml
record: job:node_cpu_usage:rate5m
expr: rate(node_cpu_seconds_total[5m])
```
- `job`: Indicates that the aggregation is per job.
- `node_cpu_usage`: Describes the metric being recorded.
- `rate5m`: Specifies that it is a 5-minute rate.

This clear and consistent naming helps when querying precomputed time series, making it easier to understand what the rule represents without needing to examine the underlying expression.

---

### Summary:
- **Recording rules** allow for precomputing and storing PromQL expressions as new time series, improving query performance and reducing complexity.
- They are particularly useful for **reducing cardinality**, **simplifying complex queries**, and **caching data** for frequently queried metrics.
- Proper **naming conventions** help maintain clarity and consistency across rules, with descriptive names that reflect scope, metric, and aggregation windows.

Recording rules should be used thoughtfully, avoiding overuse for metrics that don’t benefit from precomputation.