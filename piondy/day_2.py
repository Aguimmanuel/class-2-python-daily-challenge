student_name = input("Student name: ")
mathematics = float(input("Enter Mathematics score: "))
english = float(input("Enter English score: "))
basic_science = float(input("Enter Basic Science score: "))

total_score = mathematics + english + basic_science
average_score = total_score / 3

print( "-" * 5, "REPORT CARD", "-" * 5)
print(f"Student Name: {student_name}")
print(f"Mathematic Score: {mathematics}")
print(f"English score: {english}")
print(f"Basic science score: {basic_science}")
print(f"TOTAL: {total_score:.2f}")
print(f"AVERAGE: {average_score:.2f}")