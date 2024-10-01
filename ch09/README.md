### Chapter 9: Containers and Kubernetes (Detailed Summary)

Chapter 9 explores how Prometheus can be used to monitor containerized environments and Kubernetes clusters. Prometheus integrates well with container orchestrators and container metrics providers, making it a go-to solution for dynamic infrastructure monitoring.

#### **cAdvisor** (CPU, Memory, Labels):
**cAdvisor** (Container Advisor) is a key component of Prometheus that collects resource usage and performance metrics from containers, primarily in Kubernetes environments.
0. **Run Cadvisor**:
VERSION=v0.45.0 # use the latest release version from https://github.com/google/cadvisor/releases
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  gcr.io/cadvisor/cadvisor:$VERSION
  
1. **CPU**: 
   - cAdvisor gathers detailed CPU metrics for containers, such as CPU usage (in seconds) and CPU throttling information. These metrics help in understanding how much CPU a container is consuming and whether the container is experiencing CPU throttling due to resource limits【5†source】.
   - CPU metrics are presented in terms of time spent by containers in different modes (user mode, system mode, etc.), which are essential for performance monitoring.

2. **Memory**:
   - Memory metrics include detailed statistics on memory usage, such as total memory, memory usage by processes, cache, and swap usage. cAdvisor also tracks memory limits set on containers and monitors if any containers are being terminated due to out-of-memory (OOM) errors【5†source】.
   - These memory statistics are crucial for understanding how much memory each container is consuming and whether it is nearing its memory limit.

3. **Labels**:
   - Labels are a powerful feature of cAdvisor, allowing each container’s metrics to be tagged with meaningful information. cAdvisor automatically attaches labels such as container name, namespace, pod name, and more, providing rich context for each metric. This makes it easier to identify which containers or pods the metrics are associated with, allowing for more granular monitoring【5†source】.

#### **Kubernetes**:
Prometheus integrates deeply with Kubernetes, enabling it to monitor dynamic clusters where pods and services are created and destroyed frequently.

1. **Running in Kubernetes**:
   - Prometheus can be deployed as a **Kubernetes pod** within the cluster. This allows Prometheus to directly scrape metrics from the Kubernetes API and other components of the cluster. Prometheus can automatically discover targets (such as pods and services) and adjust to changes in the cluster without manual intervention【5†source】.
   - Running Prometheus in Kubernetes also allows it to scale alongside the cluster, providing the ability to monitor thousands of dynamic resources.

2. **Service Discovery**:
   - Kubernetes Service Discovery enables Prometheus to automatically discover pods, services, and other Kubernetes resources by querying the Kubernetes API. This means Prometheus doesn’t need a static list of targets; instead, it dynamically adapts to the current state of the cluster【5†source】.
   - This discovery process is critical in large Kubernetes environments, where manual target configuration would be cumbersome and prone to errors. Prometheus uses relabeling to filter and adjust the discovered targets.

3. **kube-state-metrics**:
   - **kube-state-metrics** is a Kubernetes component that exposes cluster state metrics. Unlike cAdvisor, which focuses on resource usage (CPU, memory, etc.), kube-state-metrics collects higher-level metrics related to the state of Kubernetes objects such as deployments, nodes, pods, and jobs【5†source】.
   - These metrics provide insight into the desired vs. current state of the cluster (e.g., number of desired replicas vs. available replicas), helping to identify discrepancies and health issues within the cluster.

#### **Alternative Deployments** (Briefly):
- Alternative deployment methods for Prometheus in Kubernetes include running Prometheus **outside** of the cluster but still scraping Kubernetes resources via the API, or using **federation** to scale Prometheus across multiple clusters.
- Some setups also use **Thanos** or **Cortex** to provide long-term storage and horizontal scalability to Prometheus, overcoming its default single-node limitations【5†source】.

### Summary:
Chapter 9 explains how Prometheus monitors containerized environments using **cAdvisor** for resource metrics and integrates deeply with **Kubernetes** through automatic service discovery and the **kube-state-metrics** component. This allows for monitoring not only resource usage but also the overall health and state of Kubernetes clusters. Alternative deployment methods provide flexibility in scaling Prometheus for large or complex environments.