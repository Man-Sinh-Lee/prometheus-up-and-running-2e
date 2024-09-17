### Chapter 3: Instrumentation (Summary)

Chapter 3 focuses on **instrumentation**, which refers to embedding metrics in your own applications using Prometheus. It provides guidelines on how to implement effective instrumentation using client libraries, as well as examples across various metrics types such as counters, gauges, summaries, and histograms.

#### Key Components of Instrumentation:
1. **Simple Example**: 
   - A basic HTTP server is implemented using Python, which exposes Prometheus metrics. The server responds to "Hello World" requests and provides metrics at `/metrics`.

2. **Counters**:
   - Counters are metrics that only increase. They are typically used to count occurrences of events (e.g., HTTP requests). An example shows how to count the number of "Hello World" requests.

3. **Gauges**:
   - Gauges represent values that can increase or decrease, like memory usage. An example demonstrates using a gauge to track the current time.

4. **Summaries**:
   - Summaries track the size or duration of events and provide count and sum values. An example shows how to measure request latency.

5. **Histograms**:
   - Histograms record observations in configurable buckets. They are useful for tracking the distribution of request durations or sizes. An example illustrates how to calculate quantiles (e.g., 95th percentile) using a histogram.

#### Approaching Instrumentation:
- **What to Instrument**: 
  - Key performance metrics to instrument include request rate, error rate, and latency (using the RED method: Rate, Errors, and Duration). For offline systems or batch jobs, metrics like queue length and processing rate (the USE method: Utilization, Saturation, and Errors) are important.
  
- **How Much to Instrument**: 
  - Instrumentation should be applied where it brings the most value. The chapter highlights avoiding over-instrumentation to prevent high resource usage. Cardinality (number of unique label combinations) is a major concern, as it can impact performance.

- **Naming Metrics**: 
  - Prometheus metric names should follow best practices such as using snake_case, including units in the name (e.g., `_seconds`, `_bytes`), and avoiding high-cardinality labels.

- **Unit Testing Instrumentation**: 
  - Basic unit tests for metrics are recommended, especially for key metrics critical to the application's functioning. For example, Python’s `get_sample_value` can be used to check if a counter increases as expected.

#### **Library Instrumentation**:

Library instrumentation refers to the process of adding metrics to libraries, which are often treated like mini-services within larger systems. Instrumentation at this level focuses on collecting useful metrics such as request rates, latencies, and error rates from these libraries, much like service instrumentation.

### **Key Insights on Library Instrumentation**:
    1. **Metrics in Libraries**: Libraries can benefit from key metrics like requests, latencies, and errors. For example, if a library is used to manage a cache, you could instrument it to measure cache hits and misses, or request failures. This helps monitor the performance of each subsystem within your application .

    2. **Mini Services Approach**: Libraries, especially those that provide crucial functionality (e.g., caching, databases), are treated as mini services with their own metrics. The metrics for these libraries typically cover their core operations and any errors that occur, giving insights into the performance of these subsystems .

    3. **Thread and Worker Pools**: Instrumenting thread or worker pools is essential, as it helps in tracking active threads, queue size, limits on threads, and any errors. This information is critical for managing the efficiency of multi-threaded or background tasks .

    4. **Error Handling**: It's common to track both total requests and errors within libraries. By collecting these metrics, you can calculate error rates and monitor system reliability. For example, libraries handling requests should be instrumented to track both successes and failures .

This type of instrumentation ensures that the inner workings of your application are visible and manageable, allowing for deeper analysis and troubleshooting.
The chapter emphasizes a pragmatic approach to instrumentation, encouraging developers to prioritize high-impact metrics that provide valuable insights into system performance and reliability.

#### Metrics naming:
- Follow rules and guidelines to avoid more obvious pitfalls
- Start with a letter, follow with letters, number, underscores, snake_case, metrics suffixes: _total, _count, _sum, _bucket
- Units: seconds, bytes, ratios.
- Metrics name should be global, avoid collisions with library, name should have meaning, distinction.
- Client libraries expose metrics relating to their runtime: Python, Java Virtual Machine, Go metrics use python, jvm and go prefixes.