# Goal = Return customers bill
# input = Price of items 
# Output = customers bill in 2 decimal places

price_rice = int(input("Price of rice per kg: "))
kg_rice = float(input("Kilograms of rice: "))
price_beans = int(input("Price of beans per kg: "))
kg_beans = float(input("Kilograms of beans: "))
price_garri = int(input("Price of garri per kg: "))
kg_garri = float(input("Kilograms of garri: "))

rice_total = kg_rice * price_rice
beans_total = kg_beans * price_beans
garri_total = kg_garri * price_garri
total_bill = rice_total + beans_total + garri_total

print("------------MARKET BILL----------")
print(f"Rice: {kg_rice}kg x N{price_rice} = N{rice_total: .2f}")
print(f"Beans: {kg_beans}kg x N{price_beans} = N{beans_total: .2f}")
print(f"Garri: {kg_garri}kg x N{price_garri} = N{garri_total: .2f}")
print("-" * 30)
print(f"TOTAL TO PAY: {total_bill: .2f}")