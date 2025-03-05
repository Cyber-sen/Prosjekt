#Median med "math"
import math
data = [1,2,3,4,5]

def median(x):
    x = sorted(x)
    n = len(x)
    mid = math.floor(n/2)
    if n%2 != 0:
        return x[mid]
    else: 
        return (x[mid-1]+[mid]) / 2.0
    
print("Median of the data set is", median(data))


#Meidan med "statistics"
import statistics

data = [1, 1, 2, 3, 4, 5]
print("Median of the data set is", statistics.median(data))



#Hyppigheten/antallet forekomster av et bestemt element
import math

data = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]

def mode(x):
    frequencies = {}
    for num in x:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    items_descending = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    return items_descending[0]

result = mode(data)
print("Most frequent number is", result[0], "with frequency", result[1])

