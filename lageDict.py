import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open("resources/Vannføring.csv", newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")

    next(csv_reader)  
    next(csv_reader)  

    startdato = "1995-01-01"
    format = "%Y-%m-%d"

    stats = {}

    #funksjonen tar snitt av siste 7 dager for å gi tomme rader en "passende" verdi
    def leggTilVerdi(stats):
        siste_7_dager = list(stats.values())[-7:]
        if len(siste_7_dager) == 7:
            return sum(siste_7_dager) / 7
        return 0  # Standardverdi hvis feil på de første radene

    for row in csv_reader:
        dato = row[0].split()[0]
        d = (datetime.strptime(dato, format) - datetime.strptime(startdato, format)).days
        
        try: 
            vannføring = float(row[1].replace(',', '.'))  # Vannføring (m³/s)
        except (ValueError, IndexError):
            vannføring = leggTilVerdi(stats)

        stats[d] = vannføring  

years = {}
sum_vannføring = 0.0
year_start_day = 0  

for i in range(len(stats)):
    if i in stats: 
        sum_vannføring += stats[i]

    year_start_day += 1
    if year_start_day == 365:
        years[i / 365] = sum_vannføring
        sum_vannføring = 0  
        year_start_day = 0 

x1 = list(stats.keys())
y1 = list(stats.values())

x2 = list(years.keys())
y2 = list(years.values())

plt.plot(x2, y2, marker='o', linestyle='-', color='b')
plt.xlabel('År siden startdato')
plt.ylabel('Årlig Vannføring (m³/s)')
plt.title('Vannføring over tid')
plt.grid(True)
plt.show()
