
student_name = input("Student name: ")
student_score = int(input("Score: "))

if 70 <= student_score <= 100:
    print(f"{student_name} scored {student_score}: A (Excellent)")
elif 60 <= student_score <= 69:
    print(f"{student_name} scored {student_score}: B (Very Good)")
    print(f"{70 - student_score} more marks to reach A")
elif 50 <= student_score <= 59:
    print(f"{student_name} scored {student_score}: C (Good)")
    print(f"{60 - student_score} more marks to reach B")
elif 45 <= student_score <= 49:
    print(f"{student_name} scored {student_score}: D (Pass)")
    print(f"{50 - student_score} more marks to reach C")
elif 0 <= student_score <= 44:
    print(f"{student_name} scored {student_score}: F (Fail)")
    print(f"{45 - student_score} more marks to reach D")
else:
    print("Invalid score")
