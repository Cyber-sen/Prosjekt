# For å bruke prosjektet:

Alle analysene er i notebooksmappen med drøftinger til slutt. Hver fil der analyserer en csvfil. Man kan bytte csv filene som man vil i notebooksene ved å skrive annet filnavn i raden som sier det, for å skape fleksibilitet.   
 
# eksempel på kontrollpanel:

#Valg av csv filer: temperatur.csv, Vannføring.csv
csvfilen = 'Vannføring.csv'
Periode = 'år'
Navn ='Vannføring'
Enhet = 'L/s'
Graf_type = 'line'
#For å gjøre om enhet til noe annet
konverteringsfaktor = 1000

#Intervall eks_format: '2024-01-01'
Slutt =None
Start = None

#True eller False (På eller av): Slår av eller på median og gjennomsnittsverdi (Mean)
Median = True
Mean = True

#Ekstremalpunkter, av eller på
MAX = True
MIN = True 

Info om enheter finner man på toppen av CSV filene 

Gå i mappen src, og kjør "lageTempDictPandas.py", "lageVannføringDictpandas.py" og "API.py".
De to første python filene renser vannføring og temperatur data for så å visualisere de. 
Og API filen gir tilgang til nåværende værdata i Trondheim.   



# Bibloteker å installere, så bruk følgene commando i terminalen:

pip install -r requirements.txt 