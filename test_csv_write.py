# a utility module for working with CSV files
import csv 

with open('employees.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Name', 'Salary', 'Age'])
    writer.writerow(['Joseph', 1_000, 31])
    writer.writerow(['Steve', 6_000, 66])

print('All done')