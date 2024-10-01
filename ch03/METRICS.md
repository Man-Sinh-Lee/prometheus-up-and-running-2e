Prometheus defines four core **metric types** for exposing various kinds of application and system metrics. Understanding these metric types—**Counters**, **Gauges**, **Histograms**, and **Summaries**—is key to instrumenting your services effectively.

### 1. **Counters**
A **Counter** is a cumulative metric that only increases over time and is reset to zero when the application restarts. It’s used for metrics that represent a quantity that can only increase or remain static (e.g., requests, errors, processed items).

#### Characteristics:
- **Monotonic**: It can only increase or reset to zero.
- **Use cases**: Count the number of requests, completed tasks, errors, retries, etc.

#### Example:
```go
counter := prometheus.NewCounter(prometheus.CounterOpts{
    Name: "http_requests_total",
    Help: "Total number of HTTP requests handled.",
})
counter.Inc() // Increment by 1
counter.Add(10) // Increment by 10
```

#### Example in action:
- **Total HTTP requests**: Every time a request is received, the counter increments.
- **Error rates**: Tracks the number of errors or failed transactions.
  
Counters are typically used when you want to know how many times an event has happened.

### 2. **Gauges**
A **Gauge** is a metric that represents a single numerical value that can arbitrarily go up or down. It’s useful for measuring values that fluctuate, like memory usage, CPU load, or temperature.

#### Characteristics:
- **Non-monotonic**: Can go up or down.
- **Use cases**: Memory usage, current number of in-progress requests, system load, or cache size.

#### Example:
```go
gauge := prometheus.NewGauge(prometheus.GaugeOpts{
    Name: "memory_usage_bytes",
    Help: "Current memory usage in bytes.",
})
gauge.Set(1000)   // Set gauge to an absolute value
gauge.Inc()       // Increment by 1
gauge.Dec()       // Decrement by 1
gauge.Add(50)     // Increment by 50
gauge.Sub(20)     // Decrement by 20
```

#### Example in action:
- **Memory usage**: Measure how much memory an application is currently using.
- **Concurrent requests**: Measure how many requests are currently in flight.
  
Gauges are typically used for measurements that change over time but are not cumulative, like current temperature or disk usage.

### 3. **Histograms**
A **Histogram** samples observations (usually things like request durations or response sizes) and counts them in configurable buckets. It allows you to observe the **distribution** of a set of values over time, such as the latency of requests.

#### Characteristics:
- Records both **sum** and **count** of observations.
- Configurable **buckets** for observing distributions.
- Allows you to calculate the **total count**, **sum**, and create visualizations such as latency percentiles or response size distributions.

#### Example:
```go
histogram := prometheus.NewHistogram(prometheus.HistogramOpts{
    Name:    "request_duration_seconds",
    Help:    "A histogram of the request duration.",
    Buckets: prometheus.DefBuckets,  // You can define your own buckets
})
histogram.Observe(1.2)  // Record a 1.2 second duration
histogram.Observe(0.5)  // Record a 0.5 second duration
```

#### Buckets:
The buckets define the range of values for which Prometheus will count observations. For example, the default buckets for request durations may be something like `0.005`, `0.01`, `0.025`, `0.05`, etc.

#### Example in action:
- **HTTP request latency**: Track how long HTTP requests take by measuring the latency in seconds and bucketing the results.
- **File sizes**: Measure the size of files or response payloads in bytes.

#### Visualization:
You can use the histogram to calculate things like the **95th percentile** of request duration, which is useful for identifying slow requests.

### 4. **Summaries**
A **Summary** is similar to a Histogram but provides **quantile** (e.g., 50th, 90th, 95th percentile) calculations directly in the metric itself. Summaries also track the total count and sum of observations, but the primary difference is that **quantiles are precomputed** in a summary rather than calculated at query time.

#### Characteristics:
- Measures **quantiles** directly.
- Records **sum** and **count** of observations.
- Provides **approximate percentiles** over a sliding window.
- More expensive than Histograms in terms of performance.

#### Example:
```go
summary := prometheus.NewSummary(prometheus.SummaryOpts{
    Name:       "request_duration_seconds",
    Help:       "A summary of the request duration.",
    Objectives: map[float64]float64{0.5: 0.05, 0.9: 0.01, 0.99: 0.001},  // Quantile objectives
})
summary.Observe(1.2)  // Record a 1.2 second duration
summary.Observe(0.5)  // Record a 0.5 second duration
```

#### Example in action:
- **Request duration**: Track how long each request takes and calculate the **95th** or **99th percentile** of latency.
- **Transaction value**: Record transaction amounts and calculate the percentiles of the amounts processed.

#### Differences between Histogram and Summary:
- **Histogram**: Buckets are pre-defined, and you can calculate percentiles at query time (flexible). Useful when you care about the distribution of values.
- **Summary**: Calculates percentiles (quantiles) on the client-side but is less flexible than histograms. Best for use cases where you know exactly which percentiles are important ahead of time.

### Summary Table of Metrics:

| Metric Type  | Increments/Decrements                  | Stores Distribution | Use Case Example                                   |
|--------------|----------------------------------------|---------------------|----------------------------------------------------|
| **Counter**  | Only increments                        | No                  | Total number of HTTP requests, errors              |
| **Gauge**    | Increments & Decrements                | No                  | Current memory usage, number of in-flight requests |
| **Histogram**| Observes samples, configurable buckets | Yes                 | Request latency, response sizes                    |
| **Summary**  | Observes samples, computes quantiles   | Yes (quantiles)     | Latency percentiles, transaction sizes             |

### Which Metric Type to Use?
- **Use Counters** when you are tracking a value that only increases.
- **Use Gauges** when you are measuring a value that can increase or decrease.
- **Use Histograms** when you need to measure the distribution of values and want to calculate percentiles in Prometheus queries.
- **Use Summaries** when you want pre-calculated quantiles (e.g., latency percentiles) but are okay with less flexibility than histograms.