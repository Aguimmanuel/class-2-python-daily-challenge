patient_name = input("Patient name: ")
patient_age = int(input("Age: "))
patient_temperature = float(input("Temperature: "))
patient_chest_condition = input("Chest pain (yes/no): ").lower()
patient_bleeding_condition = input("Heavy bleeding (yes/no): ").lower()
patient_consciousnesss = input("Conscious (yes/no): ").lower()

if patient_consciousnesss == "no" or patient_bleeding_condition == "yes" or patient_chest_condition == "yes" and patient_age >= 50:
    print(f"{patient_name} - RED: treated immediately")
elif patient_temperature >= 39.0 or patient_chest_condition == "yes" and patient_age < 50:
    print(f"{patient_name} - AMBER: seen within 30 minutes")
else:
    print(f"{patient_name} - GREEN: regular queue")