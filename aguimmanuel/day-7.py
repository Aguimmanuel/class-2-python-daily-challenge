base_fare = 15000
passenger_name = input("Passenger name: ")
passenger_age = int(input("Age: "))
luggage_weight = float(input("Luggage weight: "))
is_student = input("Student (yes/no): ")
promo_code = input("Promo code (type none if there is no code): ")

VALID_PROMO_CODE = (
    "HOLIDAY25"  # valid promo code stored in a const variable so it doesn't get changed
)

# seperation of concern is applied to place each if statement group together
if is_student == "yes":
    discount = 10
elif is_student == "no":
    discount = 0

if passenger_age >= 60:
    discount = 20
elif (
    promo_code == VALID_PROMO_CODE and passenger_age < 60
):  # promo code can be used by anyone except seniors
    discount = discount + 5
else:
    discount = discount + 0

if luggage_weight <= 20:
    luggage_fee = 0
elif 20 < luggage_weight <= 40:
    luggage_fee = 2000
elif (
    passenger_age >= 60 and luggage_weight > 40
):  # seniors get a luggage fee waiver if they carry heavy luggages
    luggage_fee = 0
else:
    luggage_fee = 4000

discount_amount = discount / 100 * base_fare
final_total = base_fare - discount_amount + luggage_fee

if passenger_age >= 10:  # only those above 10 years get a receipt printed out
    print(f"DISCOUNT: {discount}%")
    print(f"DISCOUNT AMOUNT: {discount_amount:.2f}")
    print(f"LUGGAGE FEE: {luggage_fee:.2f}")
    print(f"FINAL TOTAL: {final_total:.2f}")
else:
    print("Underage: Not allowed into the bus")
