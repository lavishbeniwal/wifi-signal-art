from wifi.scanner import scan_wifi
from art.mapper import map_signals
from art.renderer import render_art

wifi_data = scan_wifi()
visuals = map_signals(wifi_data)
render_art(visuals)
