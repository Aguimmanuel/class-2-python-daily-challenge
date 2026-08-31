basket_total = int(input("Basket total: "))
loyalty_member = input("Loyalty member (yes/no): ").lower()
promo_day = input("Promo day (yes/no): ").lower()

discount = (10/100) * 100
extra_discount = (15/100) * 100
delivery = 2500

if (basket_total >= 20000) and (loyalty_member == "yes") and (promo_day == "yes"):
    print(f"DISCOUNT: {discount}%")
    print(f"DISCOUNT AMOUNT: ₦{discount:.2f}")
    print(f"DELIVERY FEE:: ₦{delivery - delivery:.2f}")
    print(f"FINAL TOTAL: {basket_total - discount:.2f}")
elif (basket_total > 50000) and (loyalty_member == "no") and (promo_day == "yes"):
    print(f"DISCOUNT: {discount}%")
    print(f"DISCOUNT AMOUNT: ₦{discount:.2f}")
    print(f"DELIVERY FEE:: ₦{delivery - delivery:.2f}")
    print(f"FINAL TOTAL: ₦{basket_total - discount:.2f}")
elif (basket_total > 20000 and basket_total < 50000) and (loyalty_member == "no") and (promo_day == "yes"):
    print(f"DISCOUNT: 0%")
    print(f"DISCOUNT AMOUNT: ₦{discount - discount:.2f}")
    print(f"DELIVERY FEE:: ₦{delivery - delivery:.2f}")
    print(f"FINAL TOTAL: ₦{basket_total:.2f}")
elif (basket_total >= 20000) and (loyalty_member == "no") and (promo_day == "no"):
    print(f"DISCOUNT: 0%")
    print(f"DISCOUNT AMOUNT: ₦{discount - discount:.2f}")
    print(f"DELIVERY FEE:: ₦{delivery - delivery:.2f}")
    print(f"FINAL TOTAL: ₦{basket_total:.2f}")
elif (basket_total < 20000) and (loyalty_member == "yes") and (promo_day == "no"):
    print(f"DISCOUNT: 0%")
    print(f"DISCOUNT AMOUNT: ₦{discount - discount:.2f}")
    print(f"DELIVERY FEE:: ₦{delivery:.2f}")
    print(f"FINAL TOTAL: ₦{basket_total + delivery:.2f}")