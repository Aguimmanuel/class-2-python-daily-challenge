student_name = input("Student name: ")
score = int(input("Score: "))

if score < 0 or score > 100:
    print("Enter a valid score.")
elif score >= 70 and score <= 100:
    print(f"{student_name} scored {score}: A (Excellent)")
elif score >= 60 and score <= 69:
    print(f"{student_name} scored {score}: B (Very good)")
    remaining = 70 - score
    print(f"{remaining} more marks to reach A")
elif score >= 50 and score <= 59:
    print(f"{student_name} scored {score}: c (Good)")
    remaining = 60 - score 
    print(f"{remaining} more marks to reach B") 
elif score >= 45 and score <= 49:
    print(f"{student_name} scored {score}: D (pass)")
    remaining = 50 - score
    print(f"{remaining} more marks to reach C")
else:
    print(f"{student_name} scored {score}: F (Fail)")
    remaining = 45 - score
    print(f"{remaining} more marks to reach D")