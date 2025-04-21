import pandas as pd
import matplotlib.pyplot as plt
from my_packages.lesCsv import TidsseriePlotter
# import os as os




def sammenlign_plot(plot1: TidsseriePlotter, plot2: TidsseriePlotter, tittel="Sammenligning"):
    df1 = pd.DataFrame(list(plot1.data_dict.items()), columns=["Tidspunkt", "Verdi"])
    df2 = pd.DataFrame(list(plot2.data_dict.items()), columns=["Tidspunkt", "Verdi"])

    # Lager graf
    plt.figure(figsize=(12,6))
    plt.plot(df1["Tidspunkt"], df1["Verdi"], label=plot1.visningsnavn)
    plt.plot(df2["Tidspunkt"], df2["Verdi"], label=plot2.visningsnavn)

    plt.title(tittel)
    plt.xlabel("Tid")
    plt.ylabel(f"{plot1.visningsnavn} / {plot2.visningsnavn}")
    plt.legend()
    plt.grid(True)
    plt.show()
