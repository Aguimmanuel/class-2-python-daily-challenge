sales_today, total_sale, biggest_sale, average_sale = 0, 0, 0, 0

print("----- SALES TERMINAL -----")
print("1. Record a sale")
print("2. Today so far")
print("3. Close for the day")

while True:
    choice = int(input("\nChoose (1/2/3): "))
   
    if choice == 1:
        money_collected = float(input("money_collected: "))
        if money_collected >= 1:
            print("Sale recorded")
            sales_today +=1
            total_sale +=money_collected
            average_sale = total_sale/sales_today
        else:
            print("Sale must be above Zero")
        if money_collected > biggest_sale:
            biggest_sale = money_collected
            continue

    elif choice == 2:
        print(f"SALES SO FAR: {sales_today}")
        print(f"MONEY SO FAR: {total_sale:.2f}")
        print(f"BIGGEST SALE: {biggest_sale:.2f}")

    elif choice == 3:
        close = input("Type CLOSE to confirm: ")
        if close == "CLOSE":
            print(f"SALES TODAY:{sales_today} ")
            print(f"MONEY COLLECTED: {total_sale:.2f}")
            print(f"BIGGEST SALE: {biggest_sale:.2f}")
            print(f"AVERAGE SALE: {average_sale:.2f}")
            break
        else:
            print("Close cancelled - back to the terminal")
    