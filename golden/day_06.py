basket = float(input("Basket total: "))
loyalty = input("Loyalty member (yes/no): ")
promo = input("Promo day (yes/no): ")

promo_day = promo == "yes"
member = loyalty == "yes"
delivery = basket >= 20000
delivery_fee = 0

if promo_day:
    if member:
        print("DISCOUNT: 15%")
        discount_amount = (15 / 100) * basket
        print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
        if delivery:
            delivery_fee = 0
            print(f"DELIVERY FEE: N{delivery_fee:.2f}")
        else:
            delivery_fee = 2500
            print(f"DELIVERY FEE: N{delivery_fee:.2f}")
        print(f"FINAL TOTAL: N{(basket - discount_amount) + delivery_fee:.2f}")
    else:
        if basket >= 50000:
            print("DISCOUNT: 10%")
            discount_amount = (10 / 100) * basket
            print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
            print("DELIVERY FEE: N0.00")
            print(f"FINAL TOTAL: N{basket - discount_amount:.2f}")
        else:
            print("DISCOUNT: 0%")
            print("DISCOUNT AMOUNT: N0.00")
            if delivery:
                delivery_fee = 0
                print(f"DELIVERY FEE: N{delivery_fee:.2f}")      
            else:
                delivery_fee = 2500
                print(f"DELIVERY FEE: N{delivery_fee:.2f}")
            print(f"FINAL TOTAL: N{basket + delivery_fee:.2f}")    
else:
    if member:
        print("DISCOUNT: 10%")
        discount_amount = (10 / 100) * basket
        print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
        if delivery:
            delivery_fee = 0 
            print(f"DELIVERY FEE: N{delivery_fee:.2f}")    
        else:
            delivery_fee = 2500
            print(f"DELIVERY FEE: N{delivery_fee:.2f}")
        print(f"FINAL TOTAL: N{(basket - discount_amount) + delivery_fee:.2f}")
    else:
        if basket >= 50000:
            print("DISCOUNT: 5%")
            discount_amount = (5 / 100) * basket
            print(f"DISCOUNT AMOUNT: N{discount_amount:.2f}")
            print("DELIVERY FEE: N0.00")
            print(f"FINAL TOTAL: N{basket - discount_amount:.2f}")
        else:
            print("DISCOUNT: 0%")
            print("DISCOUNT AMOUNT: N0.00")
            if delivery:
                delivery_fee = 0
                print(f"DELIVERY FEE: N{delivery_fee:.2f}")
            else:
                delivery_fee = 2500
                print(f"DELIVERY FEE: N{delivery_fee:.2f}")
            print(f"FINAL TOTAL: N{basket + delivery_fee:.2f}")    