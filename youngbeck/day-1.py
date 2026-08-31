price_rice = float(input("Price of rice per kg: "))
kg_rice = float(input("Kilograms of rice: "))

price_beans = float(input("Price of beans per kg: "))
kg_beans = float(input("Kilograms of beans: "))

price_garri = float(input("Price of garri per kg: "))
kg_garri = float(input("Kilograms of garri: "))

cost_rice = price_rice * kg_rice
cost_beans = price_beans * kg_beans
cost_garri = price_garri * kg_garri

total_bill = cost_rice + cost_beans + cost_garri

print()
print(" ----- MARKET BILL ----- ")
print(f"Rice  : {kg_rice:.1f} kg x N{price_rice:.0f} = N{cost_rice:.2f}")
print(f"Beans : {kg_beans:.1f} kg x N{price_beans:.0f} = N{cost_beans:.2f}")
print(f"Garri : {kg_garri:.1f} kg x N{price_garri:.0f} = N{cost_garri:.2f}")
print("-" * 20)
print(f"TOTAL TO PAY: N{total_bill:.2f}")