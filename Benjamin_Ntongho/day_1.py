
rice_price = int(input("Enter Price of rice per kg: "))
rice_kg = float(input("Enter Kilogram of rice: "))

beans_price = int(input("Enter Price of beans per kg: "))
beans_kg = float(input("Enter kilogram of beans: "))

garri_price = int(input("Enter Price of garri per kg: "))
garri_kg = float(input("Enter kilogram of garri: "))

rice_bill = rice_price * rice_kg
beans_bill = beans_price * beans_kg
garri_bill = garri_price * garri_kg 

total_bill = rice_bill + beans_bill + garri_bill

print(" ")
print("-"*16,"MARKET BILL","-"*20)

print(f"Rice  : {rice_kg}  kg x N{rice_price}   = N{rice_bill:.2f} ")
print(f"Beans : {beans_kg}  kg x N{beans_price}   = N{beans_bill:.2f} ")
print(f"Garri : {garri_kg}  kg x N{garri_price}    = N{garri_bill:.2f} ")


print("-"*50)

print(f"TOTAL TO PAY: N{total_bill:.2f}")
