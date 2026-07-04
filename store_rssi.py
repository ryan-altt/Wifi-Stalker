import subprocess
import sys

def exec_wifi():
    return subprocess.check_output(['nmcli', 'dev', 'wifi']).decode('utf-8')

def store_rssi(name):

    wifis_line = exec_wifi()
    wifis_tab = wifis_line.splitlines()

    for line in wifis_tab:
        if name in line:
            return int(line.split()[6])

def main():
    if len(sys.argv) != 1:
        exit(84)
    print(store_rssi('GRACE_OF_GOD'))

if __name__ == "__main__":
    main()