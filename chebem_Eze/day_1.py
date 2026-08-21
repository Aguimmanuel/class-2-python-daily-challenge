# A basic market calculator for women at mile 1 Port Harcourt

print("Welcome to Market Bill calculator")

rice_price = int(input("\nWhat's today's price per kg for rice: "))
kg_rice = float(input("How many kilogram of rice: " ))

beans_price = int(input("What's today's price per kg for beans: "))
kg_beans = float(input("How many kilogram of beans: " ))

garri_price = int(input("What's today's price per kg for garri: "))
kg_garri = float(input("How many kilogram of garri: " ))

goods = {"Rice": [kg_rice, rice_price], "Beans": [kg_beans, beans_price], "Garri": [kg_garri, garri_price]}
print()
print("----- MARKET BILL -----")
total = 0
for key, value in goods.items():
    print(f"{key}: {value[0]} kg x N{value[1]} = N{(value[0]*value[1]):.2f}")
    total += value[0] * value[1]
print("-------------------------")
print(f"TOTAL TO PAY: N{total:.2f}")
