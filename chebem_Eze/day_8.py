"""This program helps an Ajo Collector carryout End Of Day analysis for their business"""

no_of_customers = int(input("Customers paying today: "))
biggest_payment, big_savers, total, count = 0, 0, 0, 0
while count < no_of_customers:
    name_of_customer = input(f"Customer {count+1} name: ")
    amount_paid = int(input("Amount paid: "))
    if amount_paid > biggest_payment:
        biggest_payment = amount_paid
        name = name_of_customer
    if amount_paid >= 10000:
        big_savers +=1 
    
    total += amount_paid
    count +=1

average = total/no_of_customers
print(f"\nTOTAL COLLECTED: N{total:.2f}")
print(f"CUSTOMERS: {no_of_customers}")
print(f"BIG SAVERS: {big_savers}")
print(f"BIGGEST PAYMENT: N{biggest_payment:.2f} by {name}")
print(f"AVERAGE PER CUSTOMER: N{average:.2f}")
