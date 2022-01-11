import csv

with open('bank.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    total = 0
    for row in reader:
        salary = int(row[1])
        total += salary
    print(f'The total of all balances is {total}')