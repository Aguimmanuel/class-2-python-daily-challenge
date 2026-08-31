age = int(input("Enter age: "))

loan = input("Unpaid loan with the bank (yes/no): ").lower()

monthly_income = int(input("What's your monthly income? "))
guarantor = input("Civil-servant guarantor (yes/no): ").lower()


if age < 21 or age > 55:
    print("DECISION: DECLINED - not within the age bracket")
elif loan == "yes":
        print("DECISION: DECLINED - unpaid loan with the bank")
elif monthly_income < 80000 and guarantor == "yes":
    print("DECISION: APPROVED - guarantor covered the income rule")
elif monthly_income >= 80000:
    print("DECISION: APPROVED - you are qualified on income")
else:
    print("DECISION: DECLINED - monthly income below range")
