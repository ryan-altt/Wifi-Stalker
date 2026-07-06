# Wifi-tracker

Wifi-tracker is a Python-based tool designed to detect movement within a room by monitoring the **RSSI (Received Signal Strength Indicator)** of a specific Wi-Fi network.

## 🚀 How it Works

The system leverages the fact that human bodies are primarily composed of water, which absorbs and reflects 2.4GHz/5GHz radio signals. When a person moves between a Wi-Fi access point and the receiver, the RSSI fluctuates.

The tool operates in two phases:
1. **Calibration Phase**: It samples the Wi-Fi signal in an empty room to establish a baseline average RSSI.
2. **Monitoring Phase**: It continuously monitors the signal. If the RSSI drops significantly below the calibrated average (exceeding a predefined margin), a movement is detected.

## ✨ Features

- **Real-time Detection**: Immediate feedback when movement is detected.
- **Data Logging**: Ability to log RSSI values over time to a CSV file for further analysis.
- **Visualization**: Integrated graphing tool using Matplotlib to visualize signal variations and smoothing.

## 🛠️ Prerequisites

- **Operating System**: Linux (required for `nmcli`).
- **Tooling**: `NetworkManager` must be installed and running (`nmcli` command).
- **Python 3.x**

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Wifi-tracker.git
   cd Wifi-tracker
   ```

2. Install the required Python libraries:
   ```bash
   pip install pandas matplotlib
   ```

## 🚀 Usage

Run the detector by specifying the name (SSID) of the Wi-Fi network you want to track:

```bash
python detector.py "Your_Wifi_Name"
```

## 📊 Data Analysis

The project includes functionality to store data in `data.csv` and generate graphs to analyze the signal stability and the impact of movement.

## ⚠️ Limitations

- **Sensitivity**: The detection depends on the environment, the distance between the AP and the receiver, and the specific Wi-Fi hardware used.
- **False Positives**: Other electronic devices or moving metal objects can also affect RSSI.
