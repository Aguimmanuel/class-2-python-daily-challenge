name = input("Student name: ")
score = int(input("Score: "))

if score < 0 or score > 100:
    print("Error: Invalid score. Please enter a whole number between 0 and 100.")
else:
    if score >= 80:
        grade = "A"
        remark = "Excellent"
    elif score >= 70:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 45:
        grade = "D"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

    print(name + " scored " + str(score) + ": " + grade + " (" + remark + ")")

    if grade == "A":
        print("A student on grade A has nothing left to chase.")
    elif grade == "B":
        marks_needed = 80 - score
        print(str(marks_needed) + " more marks to reach A")
    elif grade == "C":
        marks_needed = 70 - score
        print(str(marks_needed) + " more marks to reach B")
    elif grade == "D":
        marks_needed = 60 - score
        print(str(marks_needed) + " more marks to reach C")
    elif grade == "F":
        marks_needed = 45 - score
        print(str(marks_needed) + " more marks to reach D")