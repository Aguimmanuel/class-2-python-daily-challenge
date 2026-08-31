
# Sample run:

# Customers paying today: 3
# Customer 1 name: Chika
# Amount paid: 8000
# Customer 2 name: Emeka
# Amount paid: 15000
# Customer 3 name: Ngozi
# Amount paid: 12000

# TOTAL COLLECTED: N35000.00
# CUSTOMERS: 3
# BIG SAVERS: 2
# BIGGEST PAYMENT: N15000.00 by Emeka
# AVERAGE PER CUSTOMER: N11666.67


# Ajo Collector End Of Day — a real-world task using only today's concepts: while loops, counting with variables, 
# comparisons (==, !=, <, >, <=, >=), if / elif / else, variables, input(), converting input (int, float), 
# basic arithmetic, and printing with 2-decimal money format. No imports, no tricks.
# Mama Ngozi runs an ajo scheme in Mile 3 Market. Every evening she collects daily contributions from traders, 
# and at closing time she needs a small program to count up the day's collections.
# The program asks for the number of customers who paid today (a whole number). Then it works through them one by one: 
# for each customer it asks the customer's name and the amount paid (decimals allowed).
# While going through the customers, the program must keep track of:
# - The running total collected.
# - How many customers paid 10000 or more (Mama Ngozi calls them big savers).
# - The biggest single payment of the day and the customer who made it. If two customers tie on the biggest payment, 
# the one who paid first keeps the crown.
# After the last customer, the program prints exactly five lines: total collected, number of customers, 
# number of big savers, the biggest payment with the customer's name, and the average per customer, all money values with 
# two decimal places.

# Edge cases to handle: only one customer, a payment of exactly 10000 (a big saver), a day where nobody reaches 
# 10000 (BIG SAVERS: 0, but the biggest payment still prints), a payment of 0 (it counts as a customer), and 
# two customers tying on the biggest amount.

num_of_customers_who_paid = int(input("Customers paying today: "))
count = 1

while count <= num_of_customers_who_paid:
    
    customer_name = input(f"Customer {count} name: ")
    amount_paid = int(input("Amount paid: "))
    count += 1
    
