basket_total = float(input("Basket total: "))
is_loyalty_member = input("Loyalty member (yes/no): ").lower()
promo_day = input("Promo day (yes/no): ").lower()


if is_loyalty_member == "yes" and basket_total > 0:
    discount = 10
elif basket_total >= 50000:
    discount = 5

if promo_day == "no" and basket_total > 0:
    discount = discount + 0
elif promo_day == "yes" and (is_loyalty_member == "yes" and basket_total > 0) or basket_total >= 50000:
    discount = discount + 5
else:
    discount = 0
    
if basket_total == 0 or basket_total >= 20000:
    delivery_fee = 0
elif basket_total < 20000:
    delivery_fee = 2500

discount_amount = (discount / 100) * basket_total
final_total = (basket_total - discount_amount) + delivery_fee

print(f"DISCOUNT: {discount}%")
print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
print(f"DELIVERY FEE: N{delivery_fee:.2f}")
print(f"FINAL TOTAL: N{final_total:.2f}")