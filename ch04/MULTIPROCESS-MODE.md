### Summary of Multiprocess Mode in Prometheus Client Libraries

**Objective**: Ensure efficient and accurate metric collection in multi-process environments without the performance overhead of network communication.

**Approach**:
1. **Memory-Mapped Files (mmap)**:
   - **What**: Each process uses memory-mapped files to track its own metrics.
   - **Why**: `mmap` allows fast access to shared memory between processes without the overhead of network communication or system calls.
   - **How**: Metrics are written to these `mmap`-ed files by each process. During metric exposition (when metrics are served to Prometheus), all these files are read, and the metrics from each process are combined.

2. **Concurrency Handling**:
   - **No Locking**: There is no locking mechanism between the writing of metrics by processes and their reading during exposition. Instead, the system relies on the fact that metric values are consistently aligned in memory and uses a two-phase write approach to ensure new time series are added correctly.

3. **Counters vs. Gauges**:
   - **Counters**: Metrics like counters (and also summaries and histograms) are designed to only increase or stay the same, never decrease. To ensure accuracy, files related to counters are retained even after a worker process exits.
   - **Gauges**: Gauges can go up or down, so how they are handled can vary:
     - For metrics like "in-progress requests," which only need live process data, configurations can ensure only metrics from currently running processes are used.
     - For metrics like "last time a request was processed," where you might want the maximum value across both active and terminated processes, configurations can be adjusted accordingly.

**Summary**:
- **Performance**: Using `mmap` for inter-process communication provides fast and efficient access to metrics data without the overhead of network-based communication.
- **Isolation and Accuracy**: Metrics from multiple processes are combined without locking, and the system ensures that counters remain accurate while providing flexibility for handling gauges based on their specific needs.

This design allows Prometheus client libraries to efficiently manage and aggregate metrics in environments where multiple processes are involved, balancing performance with the accuracy of metric data.