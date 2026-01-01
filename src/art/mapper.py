def map_signals(networks):
    visuals = []

    for net in networks:
        strength = (net["rssi"] + 90) / 60
        strength = max(0.0, min(1.0, strength))

        visuals.append({
            "strength": strength,
            "freq": net["freq"]
        })

    return visuals
