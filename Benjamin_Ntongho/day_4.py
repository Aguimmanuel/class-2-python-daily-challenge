
age = int(input("Age: "))
monthly_income = float(input("Monthly income: "))
unpaid_loan_with_bank_status = input("Unpaid loan with the bank (yes/no): ").lower()
civil_servant_guarantor_status = input("Civil-servant guarantor (yes/no): ").lower()

if age < 21 or age > 55:
    print("DECISION: DECLINED - outside age limits")
elif unpaid_loan_with_bank_status == "yes":
    print("DECISION: DECLINED - unpaid loan with the bank")

else:
    if monthly_income >= 80000:
        print("DECISION: APPROVED - monthly income covered the income rule")
    elif civil_servant_guarantor_status == "yes":
        print("DECISION: APPROVED - guarantor covered the income rule")
    else:
        print("DECISION: DECLINED - insufficient income and no guarantor")
