name = input("Patient name: ")
age = int(input("Age: "))
temp = float(input("Temperature: "))
chest_pain = input("Chest pain (yes/no): ").lower()
heavy_bleeding = input("Heavy bleeding (yes/no): ").lower()
conscious = input("Conscious (yes/no): ").lower()


if conscious == "no" or heavy_bleeding == "yes" or chest_pain == "yes" and age >= 50:
    print(f"{name} - RED - treated immediately")
elif temp >= 39.9 or chest_pain == "yes" and age < 50:
    print(f"{name} - AMBER: seen within 30 minutes")
else:
    print(f"{name} - GREEN - regular queue")
