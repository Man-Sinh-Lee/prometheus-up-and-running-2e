Here's a detailed summary of Chapter 10, *Common Exporters* from the *Prometheus Up & Running* book with the relevant sections you requested:

### 1. **Consul Exporter:**
   - **Overview**: The Consul Exporter is used to extract monitoring data from a HashiCorp Consul cluster. It provides several metrics regarding the health of nodes, services, and other aspects of the Consul system.
   - **Key Metrics**:
     - `consul_up`: Checks if the Consul instance is up and running.
     - `consul_catalog_service_node_healthy`: Monitors the health status of services running on Consul nodes.
     - `consul_serf_lan_members`: Indicates the number of members in the Consul LAN cluster, which is crucial for identifying any network partition or related issues.
   - **Configuration Example**:
     - The exporter runs on port 9107 and exposes metrics at `/metrics`. Prometheus can be configured to scrape the exporter using the following configuration:
       ```yaml
       global:
         scrape_interval: 10s
       scrape_configs:
        - job_name: consul
          static_configs:
           - targets:
             - localhost:9107
       ```

### 2. **MySQLD Exporter:**
   - **Purpose**: The MySQLD exporter monitors MySQL (and MariaDB) database instances, extracting a wide variety of metrics.
   - **Key Metrics**:
     - `mysql_up`: Indicates if MySQL is reachable and whether it can be queried.
     - `mysql_global_status_*`: Extracts MySQL status metrics (e.g., active connections, cache hits).
     - `mysql_global_variables_*`: Provides MySQL configuration settings.
   - **Setup**:
     - A Prometheus user is created in MySQL to allow the exporter to collect metrics. Prometheus is then configured to scrape the exporter at port 9104.
     - **Sample Configuration**:
       ```yaml
       global:
         scrape_interval: 10s
       scrape_configs:
        - job_name: mysqld
          static_configs:
           - targets:
             - localhost:9104
       ```

### 3. **Grok Exporter:**
   - **Purpose**: The Grok Exporter converts log data into Prometheus metrics. It is particularly useful for parsing unstructured log files and creating structured metrics from them.
   - **How It Works**: 
     - Grok uses patterns (usually based on regular expressions) to parse log entries. These patterns can be customized or reused from other tools like Logstash.
   - **Key Example**: A log containing HTTP request data like `GET /foo 1.23` can be parsed into metrics such as total HTTP requests or request latency.
   - **Sample Configuration**:
     ```yaml
     global:
       config_version: 2
     input:
       type: file
       path: example.log
       readall: true
     grok:
       additional_patterns:
         - 'METHOD [A-Z]+'
         - 'PATH [^ ]+'
         - 'NUMBER [0-9.]+'
     metrics:
       - type: counter
         name: log_http_requests_total
         help: HTTP requests
         match: '%{METHOD} %{PATH:path} %{NUMBER:latency}'
         labels:
           path: '{{.path}}'
     server:
       port: 9144
     ```

### 4. **Blackbox Exporter:**
   - **Purpose**: The Blackbox Exporter allows for probing endpoints from the outside and testing their availability and responsiveness. It supports several protocols, including ICMP (ping), TCP, HTTP, and DNS.
   - **Key Probes**:
     - **ICMP**: Used to ping hosts, checking their availability via raw socket communication.
     - **TCP**: Allows checks for open TCP ports and simple communication.
     - **HTTP**: Allows checks for HTTP status codes, redirects, SSL, and more.
     - **DNS**: Allows queries to DNS servers, including TCP DNS queries.
   - **Configuration Example for ICMP Probe**:
     ```yaml
     icmp:
       prober: icmp
     ```
     - To use the ICMP module, you can visit `http://localhost:9115/probe?module=icmp&target=localhost`, and it will ping the target and provide metrics like `probe_success` and `probe_duration_seconds`.

   - **Prometheus Configuration**:
     - Prometheus can be configured to scrape the Blackbox Exporter by targeting port 9115:
       ```yaml
       scrape_configs:
        - job_name: blackbox
          static_configs:
           - targets:
             - localhost:9115
       ```

### Conclusion:
Chapter 10 outlines some of the most commonly used Prometheus exporters. Exporters like Consul and MySQLD provide insights into specific systems (e.g., Consul clusters, MySQL databases), while more generalized exporters like Grok and Blackbox allow for broader monitoring of logs or external services. Each exporter comes with its specific metrics, configuration requirements, and use cases, making them flexible tools for extending Prometheus's monitoring capabilities.