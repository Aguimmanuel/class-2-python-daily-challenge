# Basket total: 32000
# Loyalty member (yes/no): yes
# Promo day (yes/no): yes


basket_total = float(input("Basket total: "))
loyalty_member = input("Loyalty member (yes/no): ").lower()
promo_day = input("Promo day (yes/no): ").lower()

discount_value = 0
Actual_Discount = 0
delivery_fee = 0.00

if loyalty_member == "yes":
    discount_value = 10/100
elif not loyalty_member:
    discount_value = 0
elif not loyalty_member and basket_total >= 50000:
    discount_value = 5/100
if promo_day == "yes" and discount_value != 0:
    discount_value = discount_value + (5/100)
elif promo_day == "yes" and discount_value == 0:
    discount_value = 0
if basket_total < 20000:
    delivery_fee = 2500
elif basket_total >= 20000:
    delivery_fee = 0.00

discount_amount =(discount_value / 100) * basket_total

# DISCOUNT: 15%
# DISCOUNT AMOUNT: N4800.00
# DELIVERY FEE: N0.00
# FINAL TOTAL: N27200.00
print(" ")
print(f"DISCOUNT: {discount_value * 100:.0f}%")
print(f"DISCOUNT AMOUNT: N{discount_amount * 100:.2f}")
print(f"DELIVERY FEE: N{delivery_fee:.2f}") 
print(f"FINAL TOTAL: N{delivery_fee + basket_total - (discount_amount * 100):.2f}")


# Edge cases to handle: a non-member at exactly 50000 on a promo day (10% total), 
# a non-member at 49999 on a promo day (still 0%),  checked 
# a basket at exactly 20000 (free delivery),        checked
# a member with a small basket on a normal day (10%, pay delivery), and 
# a basket total of exactly 0.
