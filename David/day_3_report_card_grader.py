student_name = input("\nStudent name: ").title()

student_score = int(input("Score: "))

if student_score >= 70 and student_score <= 100:
    print(f"{student_name} scored {student_score}: A (Excellent)")
elif student_score >= 60 and student_score < 70:
    print(f"{student_name} scored {student_score}: B (Very Good)")
    print(f"{70 - student_score} more marks to reach A")
elif student_score >= 50 and student_score < 60:
    print(f"{student_name} scored {student_score}: C (Good)")
    print(f"{60 - student_score} more marks to reach B")
elif student_score >= 45 and student_score < 50:
    print(f"{student_name} scored {student_score}: D (Pass)")
    print(f"{50 - student_score} more marks to reach C")
else:
    print(f"{student_name} scored {student_score}: F (Fail)")
    print(f"{45 - student_score} more marks to reach D")