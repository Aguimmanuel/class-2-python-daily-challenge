""" SHOPKEEPER END-OF-DAY TERMINAL
    This program helps a shop keeper perform end of everyday summary sales made """

print("----- SALES TERMINAL -----")
print("1. Record a sale")
print("2. Today so far")
print("3. Close for the day")

items_count, total, highest_sale = 0, 0, 0
while True:
    options = int(input("\nChoose (1/2/3): "))
    if options == 1:
        sale_amount = float(input("Sale amount: "))
        if sale_amount > 0:
            items_count+=1
            total+=sale_amount
            print("Sale recorded")
            if highest_sale < sale_amount:
                highest_sale = sale_amount
        else:
            print("Sale must be above zero")
            continue

    elif options == 2:
        if sale_amount > 0:
            print(f"SALES SO FAR: {items_count}")
            print(f"MONEY SO FAR: N{total:.2f}")
            print(f"BIGGEST SALE: N{highest_sale:.2f}")
        else:
            print("No sales yet today")
        continue
    elif options == 3:
        confirm_reply = input("Type CLOSE to confirm: ")
        if confirm_reply == "CLOSE":
            break
        else:
            print("Close cancelled - back to the terminal")
    else:
        continue

print(f"\nSALES TODAY: {items_count}")
print(f"MONEY COLLECTED: N{total:.2f}")
print(f"BIGGEST SALE: N{highest_sale:.2f}")

if items_count <= 0:
    items_count = 1
print(f"AVERAGE SALE: N{(total/items_count):.2f}")
