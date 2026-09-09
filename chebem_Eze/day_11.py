""" Cafeteria Order Kiosk.
    This is program simplifies orders taken in a Cafeteria """

print("----- TODAY'S MENU -----")
print("1. Jollof rice - N1200")
print("2. Beans porridge - N900")
print("3. Chilled drink - N400")
print("4. Done")

items_count = 0
while True:
    options = int(input("Choose (1-4): "))
    if options == 1:
        items_count+=1
        continue
    elif options == 2:
        items_count+=1
        continue
    elif options == 3:
        items_count+=1
        continue
    elif options == 4:
        break
    else:
        print("No such option")
        continue

    