# DAY 1 OF 62 - Thursday 20 Aug 2026

# MARKET BILL CALCULATOR
# Market Bill Calculator — a real-world task using only today's concepts: variables, input(), converting input (int, float), basic arithmetic, and printing. No imports, no tricks.
# Solve it individually, then come together as a group to compare approaches. When you've finished and discussed, tell me "Day 1 done" and I'll update progress-log.txt and hold Day 2 until you ask for it. Good luck! 


# A trader at Mile 1 Market sells three items: rice, beans and garri. She wants a small program to work out a customer's total bill quickly instead of using a calculator and paper.

# The program must:
# - Ask for today's price per kg for rice, beans and garri.
# - Ask how many kg of each the customer is buying (kg can be a decimal, like 2.5).
# - Show a simple bill: the cost of each item and the total amount the customer must pay.
# - Money amounts should show two decimal places (for example N4500.00).

# Sample run:

# Price of rice per kg: 1800
# Kilograms of rice: 2.5
# Price of beans per kg: 2500
# Kilograms of beans: 1
# Price of garri per kg: 900
# Kilograms of garri: 3.5

# ----- MARKET BILL -----
# Rice  : 2.5 kg x N1800 = N4500.00
# Beans : 1.0 kg x N2500 = N2500.00
# Garri : 3.5 kg x N900  = N3150.00
# -------------------------
# TOTAL TO PAY: N10150.00

# Edge cases to handle: decimal kg (like 2.5), 0 kg of an item (that item shows N0.00), and big orders (for example 25 kg).

rice_price_per_kg = int(input("Price of rice per kg: "))
total_rice_kg = float(input("Kilograms of rice: "))

beans_price_per_kg = int(input("Price of beans per kg: "))
total_beans_kg = float(input("Kilograms of beans: "))

garri_price_per_kg = int(input("Price of garri per kg: "))
total_garri_kg = float(input("Kilograms of garri: "))

total_rice_price = rice_price_per_kg * total_rice_kg
total_beans_price = beans_price_per_kg * total_beans_kg
total_garri_price = garri_price_per_kg * total_garri_kg

grand_total = total_rice_price + total_beans_price + total_garri_price


print("----- MARKET BILL -----")
print(f"Rice : {total_rice_kg} kg X N{rice_price_per_kg} = N{total_rice_price:.2f} ")
print(f"Beans : {total_beans_kg} kg X N{beans_price_per_kg} = N{total_beans_price:.2f} ")
print(f"Garri : {total_garri_kg} kg X N{garri_price_per_kg} = N{total_garri_price:.2f} ")
print(f"TOTAL TO PAY: {grand_total:.2f}")
print("-------------------------")

