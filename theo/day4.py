age = int(input("input your age: "))
monthly_income = int(input("What is your Monthly income: "))
unpaid_loan = input("Do you have an unpaid loan? yes/no: ").lower()
civil_servant_quarantor = input("Quarantor: Are you a civil servant? yes/no: ").lower()
if age >= 21 and age <= 55 and (monthly_income >= 80000 and unpaid_loan == "no") and civil_servant_quarantor == "yes":
    print("DECISION: APPROVED ")
elif monthly_income < 80000 and civil_servant_quarantor == "yes":
    print("DECISION: APPROVED - quarantor covered the income rule")    
elif unpaid_loan == "yes":
    print("DECISION: DECLINED - unpaid loan with the bank")    
elif age < 21:
    print("DECISION: DECLINED - age must be between 21 and 55")    
else:
    print("DECISION: DECLINED")    
    
    
