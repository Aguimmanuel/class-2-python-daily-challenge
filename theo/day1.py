def ask_daily_price():
    rice_price = float(input("price of rice per kg: "))
    how_many_kg_rice = float(input("Kilograms of rice: "))
    beans_price = float(input("Price of beans per kg: "))
    how_many_kg_beans = float(input("Kilograms of beans: "))
    garri_price = float(input("price of garri per kg: "))
    how_many_kg_garri = float(input("Kilograms of garri: "))
    todays_price ={
        "beans_per_kg": beans_price,
        "rice_per_kg": rice_price,
        "garri_per_kg": garri_price
    }
    for key,value in todays_price.items():
        print(f"{key}: {value}")
    
    
    
    total_beans = beans_price * how_many_kg_beans
    total_rice = rice_price * how_many_kg_rice
    total_garri = garri_price * how_many_kg_garri
    
    print()
    print("----- MARKET BILL -----")
    print(f"rice: {how_many_kg_rice}kg * N{rice_price} = N{total_rice:.2f}")
    print(f"beans: {how_many_kg_beans}kg * N{beans_price} = N{total_beans:.2f}")
    print(f"garri: {how_many_kg_garri}kg * N{garri_price} = N{total_garri:.2f}")
    grand_total = total_beans + total_rice + total_garri
    print("--------------------------")
    print(f"TOTAL TO PAY = N{grand_total:.2f}")
ask_daily_price()