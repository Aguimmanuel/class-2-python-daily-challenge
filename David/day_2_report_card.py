

student_name = str(input("\nStudent name:\n "))
mathematics_score = float(input(f"{student_name}'s Mathematics score:\n ")) 
english_score = float(input(f"{student_name}'s English score:\n "))
basic_Science_score = float(input(f"{student_name}'s Basic Science score:\n "))


TOTAL = mathematics_score + english_score + basic_Science_score

AVERAGE = TOTAL/3

print("----- REPORT CARD -----")
print(f"Student:{student_name}")
print(f"Mathematics: {mathematics_score}")
print(f"English: {english_score}")
print(f"Basic Science: {basic_Science_score}")
print(f"TOTAL: {TOTAL:.2f}")
print(f"AVERAGE: {AVERAGE:.2f}")