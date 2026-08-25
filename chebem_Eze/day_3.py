""" This program helps a school teacher automates their grading system
by receiving the name and score for each student individually 
It prints the grade and the score the student needs to get to the next grade."""

name = input("Student name: ")
score = int(input("Subject score: "))

if 70<= score <= 100:
    print(f"{name} scored {score}: A (Excellent)")
elif 60<= score <= 69:
    print(f"{name} scored {score}: B (Very Good)")
    print(f"{70-score} more marks to reach A")
elif 50<= score <= 59:
    print(f"{name} scored {score}: C (Good)")
    print(f"{60-score} more marks to reach B")
elif 45<= score <= 49:
    print(f"{name} scored {score}: D (Pass)")
    print(f"{50-score} more marks to reach C")
elif 0<= score <= 40:
    print(f"{name} scored {score}: F (Fail)")
    print(f"{45-score} more marks to reach D")
else:
    print(f"{name}, you've entered an invalid score: {score}")
