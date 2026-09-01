name = input("Enter name: ")
age = int(input("Enter age: "))
temperature = float(input("Enter Temperature: "))
chest_pain = input("Chest Pain (yes/no): ")
heavy_bleeding = input("Heavy Bleeding (yes/no): ")
consious = input("Conscious (yes/no): ")

red = consious == "no" or heavy_bleeding == "yes" or chest_pain == "yes" and age >= 50
amber = temperature >= 39.0 or chest_pain == "yes" and age < 50

if red:
    print(f"{name} - RED: Treated Immediately")
elif amber:
    print(f"{name} - AMBER: Seen within 30 minutes")
else:
    print(f"{name} - GREEN: Normal Queue")