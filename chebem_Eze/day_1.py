while True:
    try:
        user_reply = input("Welcome to Market Bill calculator, Enter Y to continue or N to quit: ")
        if user_reply.lower() == "n":
            break
        else:
            rice_price = int(input("\nWhat's today's price per kg for rice: "))
            kg_rice = float(input("How many kilogram of rice: " ))
            beans_price = int(input("What's today's price per kg for beans: "))
            kg_beans = float(input("How many kilogram of beans: " ))
            garri_price = int(input("What's today's price per kg for garri: "))
            kg_garri = float(input("How many kilogram of garri: " ))
            break
    except ValueError as e:
        print(f"{e}, Kindly enter a valid number ")

if user_reply != "n":
    goods = {"Rice": [kg_rice, rice_price], "Beans": [kg_beans, beans_price], "Garri": [kg_garri, garri_price]}
    print()
    print("----- MARKET BILL -----")
    total = 0
    for key, value in goods.items():
        print(f"{key}: {value[0]} kg x {value[1]} kg = N{(value[0]*value[1]):.2f}")
        total += value[0] * value[1]
    print("-------------------------")
    print(f"TOTAL TO PAY: N{total:.2f}")
