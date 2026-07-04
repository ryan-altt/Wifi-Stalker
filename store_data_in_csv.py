import time
import datetime
from store_rssi import store_rssi
import sys

def store_data_in_csv(wifi_name):
    
    with open("data.csv", "a") as file:
        while True:
            rssi = store_rssi(wifi_name)
            date = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(f"{date},{rssi}\n")
            time.sleep(1)

def main():
    if len(sys.argv) != 2:
        sys.exit(84)
    store_data_in_csv(sys.argv[1])

if __name__ == '__main__':
    main()