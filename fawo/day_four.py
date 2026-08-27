# DAY 4 OF 62 - Tuesday 25 Aug 2026

# LOAN ELIGIBILITY CHECKER

# Loan Eligibility Checker — a real-world task using only today's concepts: combining conditions with and / or / not, comparisons (==, !=, <, >, <=, >=), if / elif / else, variables, input(), int() conversion, basic arithmetic, and printing. No imports, no tricks.

# Solve it individually, then come together as a group to compare approaches. Good luck!

# A microfinance bank in Port Harcourt gives quick loans to market traders. Before seeing a real officer, customers answer four questions and a small program tells them if they qualify.

# The bank's rules:
# - Age must be between 21 and 55 (both included).
# - No unpaid loan with this bank.
# - Monthly income must be at least 80000, BUT a guarantor who is a civil servant can cover the income rule. The guarantor covers ONLY income — age and loan history must always stand on their own.

# The program must:
# - Ask the four questions: age, monthly income, unpaid loan (yes/no), civil-servant guarantor (yes/no). Answers are typed in lowercase, exactly yes or no.
# - Print one decision line: DECISION: APPROVED or DECISION: DECLINED - followed by a short reason.
# - For approvals, the line must say whether the customer qualified on income alone or through the guarantor.

# Sample run 1:

# Age: 27
# Monthly income: 55000
# Unpaid loan with the bank (yes/no): no
# Civil-servant guarantor (yes/no): yes

# DECISION: APPROVED - guarantor covered the income rule

# Sample run 2:

# Age: 45
# Monthly income: 120000
# Unpaid loan with the bank (yes/no): yes
# Civil-servant guarantor (yes/no): no

# DECISION: DECLINED - unpaid loan with the bank

# Edge cases to handle: age exactly 21, age exactly 55, age 20 WITH a guarantor (must still be declined), income exactly 80000, income 79999 with no guarantor, and an unpaid loan WITH a guarantor (guarantor cannot fix that).
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