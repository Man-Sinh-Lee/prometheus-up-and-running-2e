**Chapter 15: Binary Operators** in PromQL, based on common knowledge and Prometheus usage.

### **1. Working with Scalars**

In PromQL, **scalars** represent single, constant numerical values. Binary operators allow you to perform operations between scalars or between a vector and a scalar.

#### **Arithmetic Operators**
- Arithmetic operators such as `+`, `-`, `*`, `/`, and `%` allow you to perform mathematical operations.
  
  - **Example (from the book)**:
    ```promql
    node_memory_MemFree_bytes / 1024 / 1024
    ```
    This query converts memory values from bytes to megabytes by dividing them.

  - **Real-world example**:
    ```promql
    http_requests_total * 1000
    ```
    This query multiplies the number of HTTP requests by 1000 to convert the unit (e.g., to count in milliseconds).

#### **Trigonometric Operators**
Prometheus supports trigonometric functions such as `sin()`, `cos()`, `tan()`, `atan()`, etc.

- **Example (from the book)**:
  ```promql
  sin(time() * 0.001)
  ```
  This query generates a sine wave based on the current time.

- **Real-world example**:
  These operators are not commonly used in most system monitoring contexts, but they could be applied in specific cases like signal processing.

#### **Comparison Operators**
Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) compare values and return `1` if the condition is true, `0` if false.

- **Example (from the book)**:
  ```promql
  up == 1
  ```
  This query checks if the `up` metric is equal to `1` (i.e., if the instance is up).

- **Real-world example**:
  ```promql
  node_cpu_seconds_total > 100
  ```
  This query returns a vector with `1` for instances where CPU time is greater than 100 seconds.

### **2. Vector Matching**

**Vector Matching** in PromQL refers to how two vectors are combined when performing binary operations. There are three types: one-to-one, many-to-one, and many-to-many.

#### **One-to-One Matching**
- This is the default vector matching. In one-to-one matching, each series on the left-hand side is paired with exactly one series on the right-hand side, based on matching labels.

  - **Example (from the book)**:
    ```promql
    node_memory_MemFree_bytes / node_memory_MemTotal_bytes
    node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes
    ```
    This calculates the free memory percentage by dividing memory values from vectors with the same labels.

  - **Real-world example**:
    ```promql
    sum by (job, instance) (node_cpu_seconds_total{mode="system"}) 
    /
    sum by (job, instance) (node_cpu_seconds_total)

    ```
    This query calculates the percentage of CPU time spent in "system" mode relative to the total CPU time.

#### **Many-to-One Matching**
- In **many-to-one** matching, many series on the left-hand side can match with a single series on the right-hand side. This is achieved using `group_left`.

  - **Example (from the book)**:
    ```promql
    sum without(cpu) (node_cpu_seconds_total{mode="user"}) / sum without(cpu) (node_cpu_seconds_total)    ```
    This divides calculate the total CPU time spent in user mode across all CPUs for each instance and compare it to the total CPU time across all modes.
  - **Real-world example**:
    ```promql
    sum by (job, instance) (node_cpu_seconds_total{mode="system"}) / sum by (job, instance) (node_cpu_seconds_total)
    ```
    This will provide you with the user CPU time percentage per job and instance, ensuring that you aggregate correctly based on both dimensions.

#### **Many-to-Many Matching**
- **Many-to-many** matching allows for multiple series on the left to match multiple series on the right. Logical operators are used in many-to-many matching.

  - **Example (from the book)**:
    Many-to-many vector matching often throws errors unless properly handled with logical operators.
    ```promql
    (sum by (instance) (node_memory_MemTotal_bytes) - 
    sum by (instance) (node_memory_MemFree_bytes)) 
    /
    sum by (instance) (node_memory_MemTotal_bytes)
    ```
    This will calculate the percentage of used memory relative to the total memory available on the node.
  - **Real-world example**:
    ```promql
    http_requests_total and node_cpu_seconds_total
    ```
    This query performs a logical AND between HTTP requests and CPU usage metrics, only returning series present in both vectors.
    ```promql
    sum by (instance) (node_memory_MemAvailable_bytes) 
    /
    sum by (instance) (node_memory_Buffers_bytes)
    ```
    This query compares available memory with a different metric, such as buffers
### **Logical Operators**
Logical operators such as `and`, `or`, and `unless` allow you to combine time series in various ways.

- **Example (from the book)**:
  ```promql
  up and on(instance) http_requests_total
  ```
  This query returns only the instances that are both `up` and receiving HTTP requests.

- **Real-world example**:
  ```promql
  http_requests_total or http_errors_total
  ```
  This query returns all series that have either requests or errors.

### **3. Operator Precedence**

Operator precedence in PromQL determines how expressions are grouped when multiple operators are used in a single query. Operators with higher precedence are evaluated first.

- **Precedence Order** (from highest to lowest):
  1. `^` (exponentiation)
  2. `*`, `/`, `%` (multiplication, division, modulo)
  3. `+`, `-` (addition, subtraction)
  4. Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
  5. Logical operators (`and`, `or`, `unless`)

- **Example (from the book)**:
  ```promql
  rate(http_requests_total[5m]) > 0 and up == 1
  ```
  In this query, `>` and `==` are evaluated first, followed by `and`.

- **Real-world example**:
  ```promql
  (node_memory_MemFree_bytes / node_memory_MemTotal_bytes) * 100 > 50
  ```
  This query first calculates the free memory percentage and then checks if it is greater than 50%.
  ```promql
  100 * (sum without(fstype, job) (node_filesystem_free_bytes{mountpoint="/"}) 
    /
  sum without(fstype, job) (node_filesystem_size_bytes{mountpoint="/"}))

  100 * (sum without(fstype, job) (node_filesystem_free_bytes{mountpoint="/var/lib/mysql"}) 
    /
  sum without(fstype, job) (node_filesystem_size_bytes{mountpoint="/var/lib/mysql"}))
  ```
  This will calculate the percentage of free bytes relative to total bytes for a specific mountpoint in Prometheus

### Summary:
Chapter 15 on **Binary Operators** introduces how PromQL can handle scalar operations (arithmetic, trigonometric, and comparison), and how vectors are matched and combined using binary operators. It also covers operator precedence, ensuring queries are properly executed based on logical grouping.