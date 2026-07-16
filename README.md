# Wifi-Stalker

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-GPLv3-green.svg)

A Python tool to detect human movement in a room by monitoring Wi-Fi signal RSSI variations using the NetworkManager API.

---

## 🎯 The Concept

The idea is simple: human bodies absorb and reflect radio waves (2.4GHz/5GHz). When someone walks between the Wi-Fi access point and the receiver, the RSSI fluctuates.

The script works in two phases:
1. **Calibration**: Sample the signal in an empty room to establish a baseline average (15 samples for better accuracy)
2. **Monitoring**: Continuously track the signal. If RSSI drops significantly below the calibrated average (margin of 5 dBm), movement is detected

---

## 📋 Requirements

- **Operating System**: Linux (tested on Arch Linux)
- **Dependencies**: Python 3.7+, `networkmanager` command-line tool
- **NetworkManager**: Must be installed and running

### Installation

```bash
# Install dependencies
pip install pandas matplotlib

# Verify NetworkManager is installed
nmcli --version
```

---

## 🚀 Usage

Run the detector by passing the Wi-Fi network name (SSID) to monitor:

```bash
python detector.py "Your_WiFi_Name"
```

### Example

```bash
# Monitor a specific Wi-Fi network
python detector.py "My_Home_WiFi"

# Monitor a public Wi-Fi network
python detector.py "Free_WiFi_Public"
```

---

## 📊 Data Analysis

Signal values are automatically stored in `data.csv` for later analysis. The script also generates real-time visualizations:

- **Signal Stability**: Monitors RSSI fluctuations over time
- **Movement Detection**: Visual indicators show when movement is detected
- **Threshold Monitoring**: Displays calibration baseline and detection threshold

### Sample Output

```
[PHASE DE CALIBRATION]
Calibration [1/15] [|] RSSI: -45.23
Calibration [2/15] [/] RSSI: -44.89
Calibration [3/15] [-] RSSI: -45.67
...
Calibration termine. Moyenne: -45.12

Seuil de détection: -50.12 dBm (Moyenne: -45.12 - Marge: 5)

[PHASE DE SURVEILLANCE]
#MOUVEMENT DETECTE # RSSI: -51.23 < -50.12 [|]
```

---

## 🔧 Technical Details

### RSSI (Received Signal Strength Indicator)

- Measured in dBm (decibels per milliwatt)
- More negative values indicate weaker signals
- Typical indoor Wi-Fi range: -30 dBm to -90 dBm
- Calibration baseline determines the detection threshold

### Detection Algorithm

1. **Calibration Phase** (15 samples, 0.5s delay each):
   - Collects baseline RSSI average
   - Establishes detection threshold (baseline - 5 dBm)

2. **Monitoring Phase**:
   - Continuously reads RSSI from NetworkManager
   - Compares current RSSI to threshold
   - Verifies movement after 3 consecutive drops
   - Visual feedback with animated indicators

### Configuration Options

The detection parameters can be adjusted in `detector.py`:

```python
# Calibration samples (default: 15)
for i in range(1, 16):

# Detection margin (default: 5 dBm)
margin = 5

# Sample delay in seconds (default: 0.5)
time.sleep(0.5)
```

---

## 🛡️ Use Cases

- **Room Occupancy Detection**: Automatically detect when a room becomes occupied
- **Home Automation**: Trigger lights or other devices when someone enters
- **Energy Management**: Optimize heating/cooling based on room occupancy
- **Security Monitoring**: Detect unauthorized movement in secured areas
- **Privacy Monitoring**: Observe patterns of movement in your own space

---

## ⚠️ Known Limitations

### Sensitivity Issues
- **Environment Dependent**: Performance varies significantly based on room layout, Wi-Fi hardware, and interference
- **Hardware Limitations**: Different WiFi adapters may have different sensitivity
- **Obstacles**: Thick walls, metal objects, and other interference can cause false positives

### False Positives
- **Metal Objects**: Moving metal furniture can create signal fluctuations
- **Electronic Devices**: Devices emitting RF signals (microwaves, cordless phones)
- **External Interference**: Other Wi-Fi networks operating nearby

### Practical Limitations
- **Distance**: Detection range depends on WiFi signal strength and room size
- **Body Position**: Detection effectiveness varies based on body position relative to WiFi router
- **Movement Type**: Detection works best with direct movement toward/away from router

---

## 📄 License

This project is licensed under the GNU GPLv3 License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Suggest enhancements to the detection algorithm

---

## 📧 Contact

For any questions or suggestions, please open an issue on GitHub or contact directly at ryansama.tech@gmail.com

---

## 🙏 Acknowledgments

This tool was created to demonstrate the use of NetworkManager API for IoT applications and signal analysis. The concept is inspired by research on using WiFi signal variations for occupancy detection.

---

## 📚 References

- [NetworkManager Documentation](https://developer.gnome.org/NetworkManager/stable/)
- [RSSI Wikipedia](https://en.wikipedia.org/wiki/Received-Signal-Strength_Indicator)
- [WiFi Occupancy Detection Research](https://arxiv.org/abs/1802.08527)
