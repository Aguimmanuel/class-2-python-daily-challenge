user_age = int(input("Age: "))
user_monthly_income = int(input("Monthly income: "))
loan_history = input("Unpaid loan with the bank (yes/no): ").lower()
guarantor = input("Civil-servant guarantor (yes/no): ").lower()


if user_age >= 21 and user_age <= 55 and loan_history == "no" and guarantor == "yes" and user_monthly_income >= 80000:
    print("DECISION: APPROVED")
elif user_age >= 21 and user_age <= 55 and loan_history == "no" and guarantor == "no" and user_monthly_income >= 80000:
    print("DECISION: APPROVED")
elif user_age >= 21 and user_age <= 55 and loan_history == "no" and guarantor == "no" and user_monthly_income < 80000:
    print("DECISION: DECLINED")
elif user_age >= 21 and user_age <= 55 and loan_history == "no" and guarantor == "no" and user_monthly_income < 80000:
    print("DECISION: DECLINED")