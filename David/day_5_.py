
patient_name = input("Patient name: ").title()
age = int(input("Age: "))
temperature = float(input("Temperature: "))
chest_pain = input("Chest pain (yes/no): ").lower()
heavy_bleeding = input("Heavy bleeding (yes/no): ").lower()
conscious = input("Conscious (yes/no): ").lower()

if (conscious == "no") or (heavy_bleeding == "yes") or (chest_pain == "yes") and (age >= 50):
    print(f"{patient_name} - RED: treated immediately")
elif (temperature >= 39.0) or (chest_pain == "yes") and (age < 50):
    print(f"{patient_name} - AMBER: seen within 30 minutes")
else:
    print(f"{patient_name} - GREEN: regular queue: everyone else.")
