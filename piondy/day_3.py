student_name = input("Enter student name: ")
score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 70:
    print(f"{student_name} scored {score}: A (Excellent)")
elif score >= 60:
    print(f"{student_name} scored {score}: B (Very good)\n{70 - score} more marks to reach A")
elif score >= 50:
    print(f"{student_name} scored {score}: C (Good)\n{60 - score} more marks to reach B")
elif score >= 45:
    print(f"{student_name} scored {score}: D (Pass)\n{50 - score} more marks to reach C")
else:
    print(f"{student_name} scored {score}: F (Fail)\n{45 - score} more marks to reach D")
