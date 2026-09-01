passenger_name = input("Passenger name: ")
age = int(input("Age: "))
luggage_weight = float(input("Luggage weight: "))
student = input("Student (yes/no): ").lower()
promo_code = input("Promo code: ")

bus_fare = 15000
valid_code = "HOLIDAY25"
no_code = "none"

if luggage_weight <= 20:
    luggage_fee = 0
elif luggage_weight > 20 and luggage_weight <= 40:
    luggage_fee = 2000
else:
    luggage_fee = 4000

if age >= 60:
    discount_percent = 20
    discount_amount = bus_fare - (bus_fare * 20/100)
    final_total = discount_amount + luggage_fee

if student == "yes" and  promo_code == valid_code:
    discount_percent = 15
    discount_amount = bus_fare - (bus_fare * 15/100)
    final_total = discount_amount + luggage_fee

elif student == "yes" and promo_code == no_code:
    discount_percent = 10
    discount_amount = bus_fare - (bus_fare * 10/100)
    final_total = discount_amount + luggage_fee

elif student == "no" and promo_code == valid_code:
    discount_percent = 5
    discount_amount = bus_fare - (bus_fare * 5/100)
    final_total = discount_amount + luggage_fee
elif student == "no" and promo_code == no_code:
    discount_percent = 0
    discount_amount = 0
    final_total = bus_fare + luggage_fee

if age > 10:
    print(f"DISCOUNT: {discount_percent}%")
    print(f"DISCOUNT AMOUNT: {discount_amount:.2f}")
    print(f"LUGGAGE FEE: {luggage_fee:.2f}")
    print(f"FINAL TOTAL: {final_total:.2f}")
else:
    print("Age not allowed.")
