patient_name = input("Enter patient's name: ")
age = int(input("Enter patient's age: "))
temperature = float(input("Enter patient's temperature: "))
chest_pain = input("Do patient have chest pain? (yes/no): ").lower()
heavy_bleeding = input("Do patient bleed heavily? (yes/no): ").lower()
conscious = input("Is patient concious? (yes/no): ").lower()


if conscious == "no" or heavy_bleeding == "yes" or chest_pain == "yes" and age >= 50:
    print(f"{patient_name} - RED: treated immediately")

elif temperature >= 39.0 or chest_pain == "yes" and age < 50:
    print(f"{patient_name} - AMBER: seen within 30 minutes")

else:
    print(f"{patient_name} - GREEN - regular queue")

if chest_pain != "yes" and chest_pain != "no" or heavy_bleeding != "yes" and heavy_bleeding != "no" or conscious != "yes" and conscious != "no":
    print("Answer for chest pain, heavy bleeding and consciousness must be exactly yes/no")