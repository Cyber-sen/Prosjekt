import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "resources/Vannføring.csv", 
    delimiter=";", 
    encoding="utf-8", 
    skiprows=2,  
    usecols=[0, 1],  
    names=["Tidspunkt", "Vannføring"]  
)


df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], format="%Y-%m-%d %H:%M:%SZ", errors="coerce")

df["Vannføring"] = pd.to_numeric(df["Vannføring"].astype(str).str.replace(",", "."), errors="coerce")

# Håndter manglende verdier (uke snitt)
df["Vannføring"] = df["Vannføring"].fillna(df["Vannføring"].rolling(7, min_periods=1).mean())

# Beregn årlig total vannføring
df["År"] = df["Tidspunkt"].dt.year

df["Dager siden start"] = (df["Tidspunkt"] - df["Tidspunkt"].min()).dt.days

årlig_vannføring = df.groupby("År")["Vannføring"].sum()

plt.figure(figsize=(10, 5))
plt.plot(årlig_vannføring.index, årlig_vannføring.values, marker="o", linestyle="-", color="b", label="Årlig vannføring")

plt.xlabel("År")
plt.ylabel("Total vannføring (m³/s)")
plt.title("Årlig vannføring over tid")
plt.legend()
plt.grid(True)
plt.show()
