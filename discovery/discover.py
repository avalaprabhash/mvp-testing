def discover_devices():
    devices = [
        {"ip": "192.168.1.101", "name": "LANforge-1", "status": "active"},
        {"ip": "192.168.1.102", "name": "LANforge-2", "status": "active"},
        {"ip": "192.168.1.110", "name": "LANforge-3", "status": "active"},
        {"ip": "192.168.1.120", "name": "LANforge-Debug", "status": "active"},
        # Add more devices as needed
    ]
    return devices


if __name__ == "__main__":
    discovered = discover_devices()
    print(discovered)
