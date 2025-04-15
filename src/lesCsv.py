import pandas as pd
import matplotlib.pyplot as plt

class TidsseriePlotter:
    def __init__(self, filsti: str, visningsnavn: str = "Verdi"):
        self.filsti = filsti # Sti for å finne filen
        self.visningsnavn = visningsnavn  # Hva grafen viser (f.eks. "Temperatur" eller "Vannføring")
        self.data_dict = {}

    def behandle_data(self):
        df = pd.read_csv(
            # Deler opp linjene og bruker pos0 og pos1
            self.filsti,
            delimiter=";",
            encoding="utf-8",
            skiprows=2,
            usecols=[0, 1],
            names=["Tidspunkt", "Verdi"]
        )
        
        # Konverterer tekst i "Tidspunkt"-kolonnen til datetime-objekter
        # Hvis noe ikke passer formatet, blir det satt som NaT
        df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], format="%Y-%m-%d %H:%M:%SZ", errors="coerce")

        # Konverterer "Verdi"-kolonnen fra tekst til tall
        # Først byttes komma til punktum og så forsøkes konvertering til float. Feil gir NaN
        df["Verdi"] = pd.to_numeric(df["Verdi"].astype(str).str.replace(",", "."), errors="coerce")

        # Ved mangel får verdien gjennomsnitt over forrige 7 dager
        # Ved mindre enn 7 brukes antallet før (min 1)
        df["Verdi"] = df["Verdi"].fillna(df["Verdi"].rolling(7, min_periods=1).mean())

        # Lager dict med tidspunktene og verdiene
        self.data_dict = dict(zip(df["Tidspunkt"], df["Verdi"]))

    def vis_graf(self, periode):
        if not self.data_dict:
            raise ValueError("Data er ikke behandlet ennå. Kjør behandle_data() først.")

        df = pd.DataFrame(list(self.data_dict.items()), columns=["Tidspunkt", "Verdi"])

        if periode == "dag":
            agg_df = df.copy()

        elif periode == "uke":
            df["Uke"] = df["Tidspunkt"].dt.to_period("W").apply(lambda r: r.start_time)
            # Gruppér etter uke og beregn gjennomsnitt
            agg_df = df.groupby("Uke")["Verdi"].mean().reset_index().rename(columns={"Uke": "Tidspunkt"})

        elif periode == "måned":
            df["ÅrMåned"] = df["Tidspunkt"].dt.to_period("M").dt.to_timestamp()
            # Gruppér etter måned og beregn gjennomsnitt
            agg_df = df.groupby("ÅrMåned")["Verdi"].mean().reset_index().rename(columns={"ÅrMåned": "Tidspunkt"})

        elif periode == "år":
            df["År"] = df["Tidspunkt"].dt.year
            # Gruppér etter år og beregn gjennomsnitt
            agg_df = df.groupby("År")["Verdi"].mean().reset_index().rename(columns={"År": "Tidspunkt"})

        else:
            raise ValueError("Ugyldig periode. Velg mellom: 'dag', 'uke', 'måned', 'år'")

        # Plotter grafen
        plt.figure(figsize=(12, 6))
        plt.plot(agg_df["Tidspunkt"], agg_df["Verdi"], label=f"{self.visningsnavn} ({periode})")
        plt.xlabel("Tid")
        plt.ylabel(self.visningsnavn)
        plt.title(f"{self.visningsnavn} over tid ({periode})")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

#Eksempel på bruk:
#bruk "data/tempvannføring.csv" eller "data/temperatur.csv" så valgfritt visningsnavn
graf = TidsseriePlotter("data/temperatur.csv",'temperatur')
graf.behandle_data()
graf.vis_graf("år")  # Kan også bruke "dag", "uke", eller "år"

#ved å se på temperatur kan vi se at maks og min temperatur for årene øker 
#snitttemperaturen har også økt med 2c, vi kan dermed skrive mest om temp
#vi trenger tester for klassen
#om csv ikke finnes, om den er tom, inneholder flere feil osv
#legge til analyser av grafene (min/max/mean for tidsperioder)
#bare skriv her om det er noe mer

# Slett alt under senere 
#Antar at visningsnavnet er det samme som y-aksen 
# Legg til muligheten til å endre y-akse og visningsnavnet hver for seg. 
