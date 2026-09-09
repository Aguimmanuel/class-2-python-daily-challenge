"""A program that helps price a single passenger for a Night Bus Fare Desk"""

name = input("Passenger name: ")
age = int(input("Age: "))
luggage_weight = float(input("Luggage weight: "))
student = input("Student (yes/no): ")
promo_code = input("Promo code: ")

base_fare, discount, is_senior, valid_code, is_minor = 15000, 0, False, False, False

if age < 10:
    print("You cannot enter the bus alone, please come back with your Parent.")
    is_minor = True
if age >= 60:
    is_senior = True
if promo_code == "HOLIDAY25":
    valid_code = True

if student == "yes":
    discount += 10
    if valid_code:
        discount +=5
elif valid_code:
    discount +=5

#handling luggage weight
if luggage_weight > 40:
    fee = 4000
elif 20 < luggage_weight <= 40:
    fee = 2000
elif luggage_weight <= 20:
    fee = 0

if is_senior:
    discount = 20

discount_amount = (discount/100) * base_fare
final_total = base_fare - discount_amount + fee
if not is_minor:
    print(f"\nDISCOUNT: {discount}%")
    print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
    print(f"LUGGAGE FEE: N{fee:.2f}")
    print(f"FINAL TOTAL: N{final_total:.2f}")