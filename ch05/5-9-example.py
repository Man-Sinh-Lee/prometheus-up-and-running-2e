from prometheus_client import Info
version_info = {
    "implementation": "CPython",
    "major": "3",
    "minor": "5",
    "patchlevel": "2",
    "version": "3.5.2",
}
INFO = Info("my_python", "Python platform information")
INFO.labels(version_info)