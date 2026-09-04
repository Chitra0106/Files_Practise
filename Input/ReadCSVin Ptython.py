import csv

with open(r"C:\Users\mailc\Files_Practise\Input\Weather_Card.csv") as csvdata:
    csvdata = csv.reader(csvdata)
    temperatures = []
    for row in csvdata:
        if row[1] !="Temp":
            temperatures.append(int(row[1]))
    print(temperatures)