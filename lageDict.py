import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open("resources/Vannføringtest.csv", newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    
    next(csv_reader) 
    next(csv_reader)  

    startdato = "1995-01-01"
    format = "%Y-%m-%d"

    stats = {}

    for row in csv_reader:
        dato = row[0].split()[0]
        try:
            d = (datetime.strptime(dato, format) - datetime.strptime(startdato, format)).days
            
            vannføring = float(row[1].replace(',', '.'))  # Vannføring (m³/s)
            
            stats[d] = vannføring 

        except (ValueError, IndexError):
            print(" feil i linje")
            continue  

month = {}
sum = 0.0
month_start_day = 0  

for i in range(len(stats)):
    try:
        sum += stats[i]
    except:
        print()
    month_start_day += 1
    if month_start_day == 30:
        month[i/30] = sum
        sum = 0  
        month_start_day = 0 

x1 = list(stats.keys())
y1 = [values for values in stats.values()]


x2 = list(month.keys())
y2 = [values for values in month.values()]


plt.plot(x2, y2, marker='o', linestyle='-', color='b')
plt.xlabel('Måneder siden startdato')
plt.ylabel('Månedlig Vannføring (m³/s)')
plt.title('Vannføring aggregert per måned')
plt.grid(True)
plt.show()