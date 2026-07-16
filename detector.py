import time
import datetime
import sys
import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import argparse

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# def end(key):
#     print(f"\nTouche détectée : {key}")
#     try:
#         if key.char == "q":
#             os._exit(0)
#     except AttributeError:
#         pass

def exec_wifi():
    return subprocess.check_output(
        ['nmcli', '-t', '-f', 'SSID,SIGNAL', 'dev', 'wifi']
    ).decode('utf-8')

def store_rssi(name):
    for line in exec_wifi().splitlines():
        parts = line.split(':')
        if len(parts) == 2 and parts[0] == name:
            return int(parts[1])
    return None

def store_data_in_csv(wifi_name):

    try:
        with open("data.csv", "a") as file:
            while True:
                rssi = store_rssi(wifi_name)
                date = datetime.datetime.now().isoformat()
                file.write(f"{date},{rssi}\n")
                file.flush()
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Arrêt propre, données sauvegardées.{RESET}")

def graph_from_csv():
    dataframe = pd.read_csv("data.csv", names=["DATE", "RSSI"])
    mean_val = dataframe["RSSI"].mean()
    min_val = dataframe["RSSI"].min()
    max_val = dataframe["RSSI"].max()
    std_val = dataframe["RSSI"].std()
    rssi_smooth = dataframe["RSSI"].rolling(window=5).mean()
    print(f"moyenne: {mean_val}\nmin: {min_val}\nmax: {max_val}\nstd: {std_val}")
    plt.plot(dataframe.DATE, dataframe.RSSI)
    plt.plot(dataframe.DATE, rssi_smooth, color='g')
    plt.title("Variation du RSSI en fonction de l'heure")
    plt.xlabel("HEUREs")
    plt.ylabel("RSSIs")
    plt.grid(True)
    plt.axhline(y=mean_val, color='r', linestyle="--")
    plt.show()

def detect_rssi(wifi_name):

    # #Listener for the keyboard input
    # # listener = Listener(on_press=end)
    # # listener.start()
    # print("Press q to exit\n")

    print(f"{BLUE}[PHASE DE CALIBRAGE]{RESET}")

    # Enregistrer le RSSI ambient de la piece vide et calculer sa moyenne
    samples = []
    motion_index = 0
    motion = ['|', '/', '-', '\\']
    for i in range(1, 16):
        rssi = store_rssi(wifi_name)
        samples.append(rssi)
        print(f"\rCalibration [{i}/15] [{motion[motion_index]}] RSSI: {rssi}", end="")
        motion_index = motion_index + 1
        if motion_index > 3:
            motion_index = 0
        time.sleep(0.5)
    mean_val = sum(samples) / len(samples)
    print(f"\r{GREEN}Calibration termine. Moyenne:{RESET} {mean_val:.2f}\n")

    # Entrer dans la phase de surveillance
    print(f"{BLUE}[PHASE DE SURVEILLANCE]{RESET}")
    margin = 5
    verif = 0
    threshold = mean_val - margin
    print(f"Seuil de détection: {threshold:.2f} dBm (Moyenne: {mean_val:.2f} - Marge: {margin})")

    while True:
        actual_rssi = store_rssi(wifi_name)
        if actual_rssi < threshold:
            verif = verif + 1
            if verif >= 3:
                print(f"\r{RED}#MOUVEMENT DETECTE# {RESET}RSSI: {actual_rssi} < {threshold:.2f}", end="")
            else:
                print(f"\rAnalyse... {actual_rssi} < {threshold:.2f} [{motion[motion_index]}]", end="")
        else:
            verif = 0
            print(f"\rNo detection... RSSI: {actual_rssi} > {threshold:.2f} [{motion[motion_index]}]", end="")

        motion_index = motion_index + 1
        if motion_index > 3:
            motion_index = 0
        time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description="Détecteur de mouvement RSSI WiFi")
    parser.add_argument("-w", "--wifi_name", help="Nom du réseau WiFi à surveiller")

    args = parser.parse_args()
    if args.wifi_name:
        detect_rssi(args.wifi_name) 
    if not args.wifi_name:
        parser.print_help()

if __name__ == '__main__':
    main()
