"""This program helps the hospital to determine which patient case needs treatment based on priority
"""
name = input("Patient name: ")
age = int(input("Age: "))
temp = float(input("Temperature: "))
chest_pain= input("chest pain (yes/no): ")
Heavy_bleeding = input("Heavy bleeding (yes/no): ")
conscious = input("Conscious (yes/no): ")

is_fifty_or_greater, is_conscious, is_bleeding, has_chestpain, high_temp = False, False, False, False, False
if age >= 50:
    is_fifty_or_greater = True
if temp >= 39.0:
    high_temp = True
if chest_pain == "yes":
    has_chestpain = True
if Heavy_bleeding == "yes":
    is_bleeding = True
if conscious == "yes":
    is_conscious = True

if not is_conscious or is_bleeding or has_chestpain and is_fifty_or_greater:
    message = "RED: treated immediately"
elif high_temp or has_chestpain and not is_fifty_or_greater:
    message = "AMBER: seen within 30 minutes"
else:
    message = "GREEN: regular queue"

print(f"{name} - {message}")