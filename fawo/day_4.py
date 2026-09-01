age = int(input("Enter age: "))
income = float(input("Monthly income: "))
loan_status = input("Unpaid loan(yes/no): ")
guarantor_status = input("Civil-service guarantor(yes/no): ")

loan = loan_status.lower()
guarantor = guarantor_status.lower()

if age < 21 or age > 55:
    print("DECISION: DECLINED - age not within the required range")
elif loan == "yes":
    print("DECISION: DECLINED - unpaid loan with the bank")
elif income >= 80000:
    print("DECISION: APPROVED - qualified on income alone")
elif income < 80000 and guarantor == "yes":
    print("DECISION: APPROVED - guarantor covered the income rule")
else:
    print("DECISION: DECLINED - income below required threshold and no guarantor")
                 