items = 0
total = 0

while True:
    print("----- TODAY'S MENU -----")
    print("1. Jollof rice - N1200")
    print("2. Beans porridge - N900")
    print("3. Chilled drink - N400")
    print("4. Done")

    choice = int(input("Choose (1-4): "))
    
    if choice == 1:
        print("Jollof rice added - N1200.00")
        items += 1
        total += 1200
    elif choice == 2:
        print("Beans porridge added - N900.00")
        items += 1
        total += 900
    elif choice == 3:
        print("Chilled drink added - N400.00")
        items += 1
        total += 400
    elif choice == 4:
        break
    else:
        print("No such option")

print(f"\nITEMS: {items}")
print(f"TOTAL: N{total:.2f}")