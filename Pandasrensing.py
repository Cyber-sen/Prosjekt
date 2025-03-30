import pandas as pd 
import missingno as msno
import matplotlib.pyplot as plt 


fil = pd.read_csv('resources/Vannføring.csv', skiprows=1, sep=';')


print(fil.head())


fil["Vannføring (m³/s)"] = (     # renser før numerisk konvertering 
    fil["Vannføring (m³/s)"]
    .astype(str)                      # Konverter til tekst først
    .str.strip()                      # Fjern whitespaces
    .str.replace(",", ".", regex=False)  # Hvis noen bruker , som desimal
    .str.replace(" ", "", regex=False)   # Fjern eventuelle mellomrom
)

fil["Vannføring (m³/s)"] = pd.to_numeric(fil["Vannføring (m³/s)"], errors='coerce') #Konverterer til numerisk verdi

fil["Vannføring (m³/s)"] = fil["Vannføring (m³/s)"].fillna(fil["Vannføring (m³/s)"].mean()) #Lager gjennomsnitt hvor vannføring mangler 




fil.to_csv('rensetVannføring.csv', index=False)


print('Ferdig')++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++