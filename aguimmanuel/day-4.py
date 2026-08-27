age = int(input("Age: "))
monthly_income = int(input("Monthly income: "))
unpaid_loan = input("Unpaid loan with the bank (yes/no): ").lower()
income_guarantor_is_civil_servant = input("Civil-servant guarantor (yes/no): ").lower()

if 21 <= age <= 55:
    if unpaid_loan == "no":
        if monthly_income >= 80000:
            print("DECISION: APPROVED - income up to minimum monthly income required")
        elif income_guarantor_is_civil_servant == "yes":
            print("DECISION: APPROVED - guarantor covered the income rule")
        elif income_guarantor_is_civil_servant == "no":
            print("DECISION: DECLINED - guarantor cannot cover the income rule")
        else:
            print("DECISION: DECLINED - income below minimum monthly income required")
    elif unpaid_loan == "yes":
        print("DECISION: DECLINED - unpaid loan with the bank")
else:
    print("DECISION: DECLINED - age is not within the eligible age range")