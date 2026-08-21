
customer = print("\nWelcome!, ")

Price_of_rice_per_kg = int(input("\nRice price for today: "))
Price_of_beans_per_kg = int(input("\nBeans price for today: "))
Price_of_garri_per_kg = int(input("\nGarri price for today: "))

customer_choice_1 = float(input("\nHow many Kg of Rice? "))

print(f"Today's Rice price is {Price_of_rice_per_kg} per Kg.")
customer_choice_2= float(input("\nHow many Kg of Beans? "))
print(f"Today's Rice price is {Price_of_beans_per_kg} per Kg.")

customer_choice_3= float(input("\nHow many Kg of Garri? "))

print(f"Today's Rice price is {Price_of_garri_per_kg} per Kg.")

rice_total = customer_choice_1 * Price_of_rice_per_kg
beans_total = customer_choice_2 * Price_of_beans_per_kg
garri_total = customer_choice_3 * Price_of_garri_per_kg

total_price = rice_total + beans_total + garri_total

print("\n----- MARKET BILL -----\n")
print(f"Rice  : {customer_choice_1} kg x {Price_of_rice_per_kg} = N{rice_total:.2f}")
print(f"Beans  : {customer_choice_2} kg x {Price_of_beans_per_kg} = N{beans_total:.2f}")
print(f"Garri  : {customer_choice_3} kg x {Price_of_garri_per_kg} = N{garri_total:.2f}")
print("-------------------------\n")
print(f"TOTAL TO PAY: N{total_price:.2f}")