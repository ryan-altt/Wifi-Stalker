import pandas as pd
import matplotlib.pyplot as plt
import sys

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

def main():
    if len(sys.argv) != 1:
        sys.exit(84)
    graph_from_csv()

if __name__ == "__main__":
    main()
