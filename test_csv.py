import csv
from datetime import datetime

with open('data.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['No.', 'User', 'Date'])
    for i in range(10):
        d = datetime.now()
        d = d.strftime('%Y.%m%d %H:%M:%S')
        writer.writerow([i + 1, f'User {i + 1}', d])

# minimal example for "reading" data from a csv file
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
