from threading import Lock
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server

class StateMetric(object):
    def __init__(self):
        self._resource_states = {}
        self._STATES = ["STARTING", "RUNNING", "STOPPING", "TERMINATED"]
        self._mutex = Lock()

    def set_state(self, resource, state):
        if state not in self._STATES:
            raise ValueError(f"Invalid state: {state}. Must be one of {self._STATES}.")
        with self._mutex:
            self._resource_states[resource] = state

    def collect(self):
        family = GaugeMetricFamily("resource_state",
                                    "The current state of resources.",
                                    labels=["state", "resource"])
        with self._mutex:
            for resource, state in self._resource_states.items():
                for s in self._STATES:
                    family.add_metric([s, resource], 1 if s == state else 0)
        yield family

if __name__ == '__main__':
    # Start the HTTP server for Prometheus to scrape
    start_http_server(8000, addr='192.168.1.111')

    # Create a StateMetric instance and register it
    sm = StateMetric()
    REGISTRY.register(sm)

    # Use the StateMetric to set the state
    sm.set_state("blaa", "RUNNING")

    import time
    try:
        while True:
            time.sleep(1)  # Keep the server running
    except KeyboardInterrupt:
        print("Shutting down...")
