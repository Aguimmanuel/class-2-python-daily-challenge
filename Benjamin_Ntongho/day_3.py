name = input("Student name: ")
score = int(input("Score: "))

if score >= 70 and score <= 100:
    print(f"{name} scored {score}: A (Excellent)")

elif score >= 60 and score <= 69:
    print(f"{name} scored {score}: B (Very Good)")
    print(f"{70 - score } more marks to reach A")

elif score >= 50 and score <= 59:
    print(f"{name} scored {score}: C (Good)")
    print(f"{60 - score } more marks to reach B")

elif score >= 40 and score <= 49:
    print(f"{name} scored {score}: D (Pass)")
    print(f"{50 - score } more marks to reach C")

elif score >= 0 and score <= 44:
    print(f"{name} scored {score}: F (Fail)")
    print(f"{40 - score } more marks to reach D")
else:
    print("Invalid Score")


