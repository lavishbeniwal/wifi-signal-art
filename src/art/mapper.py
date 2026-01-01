def map_signals(networks):
    visuals = []

    for net in networks:
        strength = (net["rssi"] + 90) / 60

        visuals.append({
            "strength": strength,
            "freq": net["freq"]
        })

    return visuals
