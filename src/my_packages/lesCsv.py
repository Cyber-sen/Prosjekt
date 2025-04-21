import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandasql as ps

class TidsseriePlotter:
    def __init__(self, filsti: str,enhet: str , periode: str = 'år', konvertering: float = 1, visningsnavn: str = "Verdi", start: str=None, slutt: str=None ):
        self.filsti = filsti # Sti for å finne filen
        self.visningsnavn = visningsnavn  # Hva grafen viser (f.eks. "Temperatur" eller "Vannføring")
        self.periode = periode #dag, uke, måned eller år, for å endre antall datapunkter etter behov
        self.enhet = enhet #Enheten til grafen
        self.konvertering = konvertering
        self.start=start
        self.slutt=slutt
        self.data_dict = {}
        self.behandle_data()

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
        
        #begrenser område som analyseres
        query = f"""
        SELECT * FROM df
        WHERE 1=1
        {f"AND Tidspunkt >= '{self.start}'" if self.start is not None else ""}
        {f"AND Tidspunkt <= '{self.slutt}'" if self.slutt is not None else ""}
        """

        df = ps.sqldf(query, locals())


        # Konverterer tekst i "Tidspunkt"-kolonnen til datetime-objekter
        # Hvis noe ikke passer formatet, blir det satt som NaT
        df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], format="%Y-%m-%d %H:%M:%SZ", errors="coerce")


        # Konverterer "Verdi"-kolonnen fra tekst til tall
        # Først byttes komma til punktum og så forsøkes konvertering til float. Feil gir NaN
        df["Verdi"] = pd.to_numeric(df["Verdi"].astype(str).str.replace(",", "."), errors="coerce")

        # Ved mangel får verdien gjennomsnitt over forrige 7 dager
        # Ved mindre enn 7 brukes antallet før (min 1)
        df["Verdi"] = df["Verdi"].fillna(df["Verdi"].rolling(7, min_periods=1).mean())
       

       #fikser alle nan om det er noen
        # df["Verdi"] = df["Verdi"].ffill().bfill()

        # Lager dict med tidspunktene og verdiene
        self.data_dict = dict(zip(df["Tidspunkt"], df["Verdi"]))

       


        # Konverterer 
        if isinstance(self.konvertering, (int, float)):
            self.data_dict = {t: v * self.konvertering for t, v in self.data_dict.items()}
       

    def agg_df(self):
        df = pd.DataFrame(list(self.data_dict.items()), columns=["Tidspunkt", "Verdi"])

        if self.periode == "dag":
            return df.copy()
        elif self.periode == "uke":
            df["Uke"] = df["Tidspunkt"].dt.to_period("W").apply(lambda r: r.start_time)
            return df.groupby("Uke")["Verdi"].mean().reset_index().rename(columns={"Uke": "Tidspunkt"})
        elif self.periode == "måned":
            df["ÅrMåned"] = df["Tidspunkt"].dt.to_period("M").dt.to_timestamp()
            return df.groupby("ÅrMåned")["Verdi"].mean().reset_index().rename(columns={"ÅrMåned": "Tidspunkt"})
        elif self.periode == "år":
            df["År"] = df["Tidspunkt"].dt.year
            return df.groupby("År")["Verdi"].mean().reset_index().rename(columns={"År": "Tidspunkt"})
        else:
            raise ValueError("Ugyldig periode. Velg mellom: 'dag', 'uke', 'måned', 'år'")

    def mean_value(self):

        # df = pd.DataFrame(list(self.data_dict.items()), columns=["Tidspunkt", "Verdi"])

        return float(np.mean(self.agg_df()["Verdi"]))

    
    def median_value(self):
        
        # df = pd.DataFrame(list(self.data_dict.items()), columns=["Tidspunkt", "Verdi"])
        return float(np.median(self.agg_df()["Verdi"]))
    

    def standardavvik(self):
        return float(np.std(self.agg_df()["Verdi"]))


    def vis_graf(self, mean=True, median = True, maximum = True, minimum = True, maxverdi:float=None, minverdi: float =None):
        if not self.data_dict:
            try:
                self.behandle_data()
            except:
                raise ValueError("Data er ikke behandlet riktig ennå. Kjør eller fiks behandle_data() først.")

        df = pd.DataFrame(list(self.data_dict.items()), columns=["Tidspunkt", "Verdi"])
       
        if minverdi is not None:
            self.data_dict = {t: v for t, v in self.data_dict.items() if v >= minverdi}

        if maxverdi is not None:
            df = df[df["Verdi"] <= maxverdi]

        # print(df["Verdi"].isna().sum()) 

          # Plotter grafen
        plt.figure(figsize=(12, 6))
        if mean==True:
            plt.axhline(self.mean_value(), color='orange', linestyle=':', label=f"Mean: {self.mean_value():.5f}")

        if median==True:
            plt.axhline(self.agg_df()['Verdi'].median(), color='red', linestyle=':', label=f"Median: {self.agg_df()['Verdi'].median():.5f}")
           
        if maximum == True:
             plt.axhline(self.agg_df()['Verdi'].max(), color='black', linestyle=':', label=f"maximum: {self.agg_df()['Verdi'].max():.5f}")

        if minimum == True:
             plt.axhline(self.agg_df()['Verdi'].min(), color='black', linestyle=':', label=f"minimum: {self.agg_df()['Verdi'].min():.5f}")

        plt.plot([], [], ' ', label=f'Std.avvik: {self.standardavvik():.5f}')
        plt.plot(self.agg_df()["Tidspunkt"], self.agg_df()["Verdi"], label=f"{self.visningsnavn} ({self.periode})")
        plt.xlabel("Tid")
        plt.ylabel(f'{self.visningsnavn} ({self.enhet})')
        plt.title(f"{self.visningsnavn} over tid ({self.periode})")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

#Eksempel på bruk:
#bruk "data/tempvannføring.csv" eller "data/temperatur.csv" så valgfritt visningsnavn
# graf = TidsseriePlotter("data/temperatur.csv",'temperatur')
# graf.behandle_data()
# graf.vis_graf("år")  # Kan også bruke "dag", "uke", eller "år"

#ved å se på temperatur kan vi se at maks og min temperatur for årene øker 
#snitttemperaturen har også økt med 2c, vi kan dermed skrive mest om temp
#vi trenger tester for klassen
#om csv ikke finnes, om den er tom, inneholder flere feil osv
#legge til analyser av grafene (min/max/mean for tidsperioder)
#bare skriv her om det er noe mer

# Slett alt under senere 
#Antar at visningsnavnet er det samme som y-aksen 
# Legg til muligheten til å endre y-akse og visningsnavnet hver for seg. 
