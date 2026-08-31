rice_price = float(input("Price of rice per kg: "))
rice_kg = float(input("Kilograms of rice: "))

beans_price = float(input("Price of beans per kg: "))
beans_kg = float(input("Kilograms of beans: "))

garri_price = float(input("Price of garri per kg: "))
garri_kg = float(input("Kilograms of garri: "))

# Calculate costs
rice_cost = rice_price * rice_kg
beans_cost = beans_price * beans_kg
garri_cost = garri_price * garri_kg

total = rice_cost + beans_cost + garri_cost

# Display bill
print("\--------------------- MARKET BILL ------------------------")
print(f"Rice  : {rice_kg:.1f} kg x N{rice_price} = N{rice_cost:.2f}")
print(f"Beans : {beans_kg:.1f} kg x N{beans_price} = N{beans_cost:.2f}")
print(f"Garri : {garri_kg:.1f} kg x N{garri_price} = N{garri_cost:.2f}")
print("--------------------------------------------------------------")
print(f"TOTAL TO PAY: N{total:.2f}")