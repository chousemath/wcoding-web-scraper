# create 2 python files

# FIRST PYTHON FILE
# Use the input() function to receive
# a person's name, bank balance, and id number
# you want to do this 3 times
# you want to write all of this data into a csv file
# called bank_balances.csv
import csv

with open('bank.csv', 'w') as a: 
    writer = csv.writer(a, delimiter= ',')
    writer.writerow(['Name', 'Bank Balance', 'ID'])
    for _ in range(3):
        name = input('What is your name?:' )
        balance = input('What is your bank balance?:' )
        id = input('What is your ID number?:' )
        writer.writerow([name, balance, id])

#with open('bank.csv', 'w') as a: 
#    writer = csv.writer(a, delimiter= ',')
#    writer.writerow(['Name', 'Bank Balance', 'ID'])
#    for _ in range(3):
#        name = input('What is your name?:' )
#        balance = input('What is your bank balance?:' )
#        id = input('What is your ID number?:' )
#        writer.writerow([name, balance, id])

# SECOND PYTHON FILE
# in a separate python file
# read all the rows of data from that bank_balances.csv
# file, and calculate the total amount in all
# bank balance, and print out that number