import random

def simulate_scan(num_networks=12):
    networks = []
    for _ in range(num_networks):
        networks.append({
            "rssi": random.randint(-90, -30),
            "freq": random.choice([2.4, 5.0]),
            "noise": random.random()
        })
    return networks
