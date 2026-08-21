student_name = input("Student name: ")
math_score = float(input("Mathematics score: "))
english_score = float(input("English score: "))
science_score = float(input("Basic Science score: "))

average = (math_score + english_score + science_score) / 3
total = math_score + english_score + science_score

print("----- REPORT CARD -----")
print(f"Student: {student_name}")
print(f"Mathematics: {math_score}")
print(f"English: {english_score}")
print(f"Basic Science: {science_score}")
print(f"TOTAL: {total:.2f}")
print(f"AVERAGE: {average:.2f}")