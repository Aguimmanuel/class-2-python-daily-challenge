# TERM REPORT AVERAGE
student_name = input("Student name: ")
mathematics_score = float(input("Mathematics score: "))
english_score = float(input("English score: "))
basic_science_score = float(input("Basic Science score: "))

student_total_score = mathematics_score + english_score + basic_science_score
student_average_score = student_total_score / 3

print("----- REPORT CARD -----")
print(f"Student: {student_name}")
print(f"Mathematics: {mathematics_score}")
print(f"English: {english_score}")
print(f"Basic Science: {basic_science_score}")
print(f"TOTAL: {student_total_score:.2f}")
print(f"AVERAGE: {student_average_score:.2f}")
