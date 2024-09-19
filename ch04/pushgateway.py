from prometheus_client import CollectorRegistry, Gauge, pushadd_to_gateway
import time

registry = CollectorRegistry()
duration = Gauge('my_job_duration_seconds',
                 'Duration of my batch job in seconds', registry=registry)

def stress_test():
    # Simulating a CPU-bound workload.
    total = 0
    for i in range(10**7):
        total += i * i  # Simple computation to increase CPU load
    return total

try:
    with duration.time():
        # Replace pass with the stress test
        result = stress_test()
        print(f"Stress test completed with result: {result}")

    # This only runs if there wasn't an exception. 
    g = Gauge('my_job_last_success_seconds',
              'Last time my batch job successfully finished', registry=registry)
    g.set_to_current_time()
finally:
    pushadd_to_gateway('192.168.1.111:9091', job='batch', registry=registry)
