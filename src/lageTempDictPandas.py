import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


df = pd.read_csv(
    "data/123.38.0-Vanntemperatur-dogn-v1.csv", 
    delimiter=";", 
    encoding="utf-8", 
    skiprows=2,  
    usecols=[0, 1],  
    names=["Tidspunkt", "Temperatur"]  
)


df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], format="%Y-%m-%d %H:%M:%SZ", errors="coerce")
df["Temperatur"] = pd.to_numeric(df["Temperatur"].astype(str).str.replace(",", "."), errors="coerce")


df["Temperatur"] = df["Temperatur"].fillna(df["Temperatur"].rolling(7, min_periods=1).mean())


df["År"] = df["Tidspunkt"].dt.year
df["Måned"] = df["Tidspunkt"].dt.month


månedlig_temp = df.groupby(["År", "Måned"])["Temperatur"].mean().unstack(level=0)


år_list = sorted(månedlig_temp.columns)


colors = cm.viridis(np.linspace(0, 1, len(år_list)))

plt.figure(figsize=(12, 6))
for i, år in enumerate(år_list):
    plt.plot(månedlig_temp.index, månedlig_temp[år], marker="o", linestyle="-", color=colors[i], label=f"{år}")

plt.xlabel("Måned")
plt.ylabel("Gjennomsnittstemperatur")
plt.title("Gjennomsnittstemperatur per måned over flere år")
plt.legend(title="År", loc="upper right", fontsize="small")
plt.grid(True)
plt.show()
