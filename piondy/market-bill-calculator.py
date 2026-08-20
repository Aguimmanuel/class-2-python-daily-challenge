def market_calculator():
    rice_price = float(input("price of Rice: "))
    rice_kg = float(input("How many kg?: "))

    beans_price = float(input("Price of Beans: "))
    beans_kg = float(input("How many kg?: "))

    garri_price = float(input("Price of Rice: "))
    garri_kg = float(input("How many kg?: "))

    price_of_rice = rice_price * rice_kg
    price_of_beans = beans_price * beans_kg
    price_of_garri = garri_price * garri_kg

    total_price = price_of_rice + price_of_beans + price_of_garri

    #print("Market price")
    print("=" * 40)
    print("\t\tMarket BIll")
    print("=" * 40)
    print(f"Price of Rice: {rice_kg}kg x {rice_price} = N{price_of_rice:.2f}")
    print(f"Price of Beans: {beans_kg} x {beans_price} = N{price_of_beans:.2f}")
    print(f"Price of Garri: {garri_kg} x {garri_price} = N{price_of_garri:.2f}")
    print(f"TOTAL TO PAY: N{total_price:.2f}")

    print("=" * 40)

market_calculator()