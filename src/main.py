from wifi.simulator import simulate_scan
from art.mapper import map_signals
from art.renderer import render_art

wifi_data = simulate_scan()
visuals = map_signals(wifi_data)
render_art(visuals)
