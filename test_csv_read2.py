import csv

with open('employees.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        print(row[0], int(row[1]) * 9_000, row[2])