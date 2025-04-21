import pandas as pd
import matplotlib.pyplot as plt
from .lesogplottCsv import TidsseriePlotter





def sammenlign_plot(plot1: TidsseriePlotter, plot2: TidsseriePlotter, tittel="Sammenligning"):
    df1 = plot1.agg_df()
    df2 = plot2.agg_df()


    plt.figure(figsize=(12, 6))

    # Velg riktig plot for plot1
    if plot1.graf_type == 'line':
        plt.plot(df1["Tidspunkt"], df1["Verdi"], label=plot1.visningsnavn)
    elif plot1.graf_type == 'bar':
        plt.bar(df1["Tidspunkt"], df1["Verdi"], alpha=0.5, label=plot1.visningsnavn)
    elif plot1.graf_type == 'scatter':
        plt.scatter(df1["Tidspunkt"], df1["Verdi"], label=plot1.visningsnavn)

    # Velg riktig plot for plot2
    if plot2.graf_type == 'line':
        plt.plot(df2["Tidspunkt"], df2["Verdi"], label=plot2.visningsnavn)
    elif plot2.graf_type == 'bar':
        plt.bar(df2["Tidspunkt"], df2["Verdi"], alpha=0.5, label=plot2.visningsnavn)
    elif plot2.graf_type == 'scatter':
        plt.scatter(df2["Tidspunkt"], df2["Verdi"], label=plot2.visningsnavn)

    assert plot2.periode == plot1.periode, 'Plotene må ha lik periode'


    plt.title(tittel)
    plt.xlabel("Tid")
    plt.ylabel(f"{plot1.visningsnavn} / {plot2.visningsnavn}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
