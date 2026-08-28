name = input("Enter name: ")
score = int(input("Enter score: "))

print(f"Student name: {name}")
print(f"Score: {score}")

excellent = score >= 70 and score <= 100
very_good = score >= 60 and score <= 69
good = score >= 50 and score <= 59
pass_grade = score >= 45 and score <= 49
fail = score >= 0 and score <= 44

if excellent:
    print(f"{name} scored {score}: A (Excellent)")
    print("Best Grade Achieved")
elif very_good:
    print(f"{name} scored {score}: B (Very Good)")
    print(f"{70 - score} more marks to reach A")
elif good:
    print(f"{name} scored {score}: C (Good)")
    print(f"{60 - score} more marks to reach B")
elif pass_grade:
    print(f"{name} scored {score}: D (Pass)")
    print(f"{50 - score} more marks to reach C")
elif fail:
    print(f"{name} scored {score}: F (Fail)")
    print(f"{45 - score} more marks to reach D")
else:
    print("Invalid Score - Scores must be from 0 - 100")