# Wifi-Stalker

A Python tool to detect human movement in a room by monitoring Wi-Fi signal RSSI variations.

## The Concept

The idea is simple: human bodies absorb and reflect radio waves (2.4GHz/5GHz). When someone walks between the Wi-Fi access point and the receiver, the RSSI fluctuates.

The script works in two phases:
1. **Calibration**: Sample the signal in an empty room to establish a baseline average.
2. **Monitoring**: Continuously track the signal. If RSSI drops significantly below the calibrated average, movement is detected.

## Quick Setup

The project runs on Linux (requires `nmcli` and NetworkManager).

```bash
# Install dependencies
pip install pandas matplotlib
```

## Usage

Run the detector by passing the Wi-Fi network name (SSID) to monitor:

```bash
python detector.py "Your_WiFi_Name"
```

## Data Analysis

Signal values are stored in `data.csv`. The script also generates charts using Matplotlib to analyze signal stability and the actual impact of movements.

## Known Limitations

- **Sensitivity**: Highly dependent on environment and Wi-Fi hardware used.
- **False Positives**: Other moving metal objects or electronic devices can interfere with the signal.
