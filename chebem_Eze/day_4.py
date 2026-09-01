""" This program determines if a user is qualified for a loan. It also specified the reason the user is qualified or not qualified"""

age = int(input("Age: "))
income = int(input("Monthly income: "))
loan_status = input("Unpaid loan with the bank (yes/no): ")
guarantor_status = input("Civil-servant guarantor (yes/no): ")

is_adult  = False
debtor = False
is_income_valid = False
is_there_a_guarantor = False

if 21<= age <= 55:
    is_adult = True
if income >= 80000:
    is_income_valid = True
if loan_status == "yes":
    debtor = True
if guarantor_status == "yes":
    is_there_a_guarantor = True   

if is_adult and not debtor:
    if is_income_valid:
        print("DECISION: APPROVED - your income is sufficient")
    elif is_there_a_guarantor:
        print("DECISION: APPROVED - guarantor covered the income rule")
elif not is_adult:
    print("DECISION: DECLINED - you're not yet an Adult")
elif debtor:
    print("DECISION: DECLINED - unpaid loan with the bank")
else:
    print("DECISION: DECLINED - Low income, no guarantor")
