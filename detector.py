import time
import datetime
from store_rssi import store_rssi
import sys
from pynput.keyboard import Key, Listener
import os

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
    for i in range(1, 10):
        rssi = store_rssi(wifi_name)
        samples.append(rssi)
        print(f"\rCalibration [{i}/10] [{motion[motion_index]}]", end="")
        motion_index = motion_index + 1
        if motion_index > 3:
            motion_index = 0
        time.sleep(1)
    mean_val = sum(samples) / len(samples)
    print(f"\r{GREEN}Calibration termine. Moyenne:{RESET} {mean_val}\n")

    # Entrer dans la phase de surveillance
    print(f"{BLUE}[PHASE DE SURVEILLANCE]{RESET}")
    margin = 10
    verif = 0
    while True:
        actual_rssi = store_rssi(wifi_name)
        if actual_rssi < (mean_val - margin):
            verif = verif + 1
            if verif >= 3:
                print(f"\r{RED}#MOUVEMENT DETECTE#{RESET}", end="")
        else:
            verif = 0
            print(f"\rNo detection... [{motion[motion_index]}]", end="")
        motion_index = motion_index + 1
        if motion_index > 3:
            motion_index = 0
        time.sleep(1)


def main():
    if len(sys.argv) != 2:
        sys.exit(84)
    detect_rssi(sys.argv[1])

if __name__ == '__main__':
    main()