""" Cafeteria Order Kiosk.
    This is program simplifies orders taken in a Cafeteria """

print("----- TODAY'S MENU -----")
print("1. Jollof rice - N1200")
print("2. Beans porridge - N900")
print("3. Chilled drink - N400")
print("4. Done")

items_count, total, jollof_price, beans_price, drink_price = 0, 0, 1200, 900, 400
while True:
    options = int(input("Choose (1-4): "))
    if options == 1:
        items_count+=1
        total+=jollof_price
        print("Jollof rice added - N1200.00")
        continue
    elif options == 2:
        items_count+=1
        print("Beans porridge added - N900")
        total+=beans_price
        continue
    elif options == 3:
        items_count+=1
        print("Chilled drink added - N400.00")
        total+=drink_price
        continue
    elif options == 4:
        break
    else:
        print("No such option")
        continue

print(f"\nITEMS: {items_count}")
print(f"TOTAL: N{total:.2f}") 