age = int(input("Enter Age: "))
income = int(input("Enter Monthly Income: "))
loan_status = input("Unpaid loan at the bank (yes/no): ")
civil_status = input("Civil Servant guarantor (yes/no): ")

valid_age = age >= 21 and age <= 55
valid_income = income >= 80000

if valid_age:
    if loan_status == "no":
        if valid_income:
            print("Decision: APPROVED - Income requirements met")
        else:
            if civil_status == "yes":
                print("Decision: APPROVED - guarantor covered the income rule")
            else:
                print("Decision: DECLINED - Income requirements not met")
    else:
        print("Unpaid loan with the bank")
else:
    print("Invalid age - Must be between 21 - 55")