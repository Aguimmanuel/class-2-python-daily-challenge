basket_total = float(input("Basket total: "))
loyalty_member = input("Loyalty member (yes/no): ").lower()
promo_day = input("Promo day (yes/no): ").lower()

discount_approved = False
if basket_total <= 0:
    delivery_fee = 0
elif basket_total < 20000:
    delivery_fee = 2500
else:
    delivery_fee = 0

if loyalty_member == "yes" and basket_total > 0:
    discount_percent = 10
    discount_approved = True
    discount_amount = (basket_total * (discount_percent / 100))
    final_total = basket_total - (basket_total * (discount_percent / 100)) + delivery_fee
    if promo_day == "yes":
        discount_percent = 15
        discount_amount = (basket_total * (discount_percent / 100))
        final_total = basket_total - (discount_amount + delivery_fee)

elif loyalty_member == "no" and basket_total >= 50000:
    discount_percent = 5
    discount_approved = True
    discount_amount = (basket_total * (discount_percent / 100))
    final_total = basket_total - (basket_total * (discount_percent / 100)) + delivery_fee
elif loyalty_member == "no" and promo_day == "no":
    discount_percent = 0
    discount_approved = False
    discount_amount = basket_total * (discount_percent / 100)
    final_total = basket_total - (basket_total * (discount_percent / 100)) + delivery_fee
    if promo_day == "yes" and basket_total > 0:
        discount_percent = 10
        discount_amount = basket_total - (basket_total * (discount_percent / 100))
        final_total = basket_total - (basket_total * (discount_percent / 100)) + delivery_fee
else:
    discount_percent = 0
    discount_approved = False
    discount_amount = basket_total * (discount_percent / 100)
    final_total = basket_total - (basket_total * (discount_percent / 100)) + delivery_fee   

print(f"DISCOUNT: {discount_percent}%")
print(f"DISCOUNT AMOUNT: {discount_amount:.2f}")
print(f"DELIVERY FEE: {delivery_fee:.2f}")
print(f"FINAL TOTAL: {final_total:.2f}")





    