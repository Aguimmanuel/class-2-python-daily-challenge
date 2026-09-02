"""This helps a supermarket anywhere in the World
 to calculate discount based on basket total, loyalty member, and promo day.
 Note: You must use lower case when entering yes/no to get accurate output"""

basket_total = float(input("Basket total: "))
loyalty_member = input("Loyalty member (yes/no): ")
promo_day = input("Promo day (yes/no): ")

is_loyal_member, is_promo_day, valid_order, delivery_fee, discount = False, False, False, 0, 0
if loyalty_member == "yes":
    is_loyal_member = True
if promo_day == "yes":
    is_promo_day = True
if basket_total > 0:
    valid_order = True

#handliing delivery fee seperately
if basket_total >= 20000:
    delivery_fee = 0
elif 0 < basket_total < 20000:
    delivery_fee = 2500

if is_loyal_member and valid_order:
    discount += 10
    if is_promo_day and discount > 0:
        discount += 5
    discount_amount = (discount * basket_total)/100
    total_pay = basket_total - discount_amount + delivery_fee
else:
    if basket_total >= 50000:
        discount +=  5
    if is_promo_day and discount > 0:
        discount += 5
    discount_amount = (discount/100) * basket_total
    total_pay = basket_total - discount_amount + delivery_fee

print(f"\nDISCOUNT: {discount}%")
print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
print(f"DELIVERY FEE: N{delivery_fee:.2f}")
print(f"FINAL TOTAL: N{total_pay:.2f}")