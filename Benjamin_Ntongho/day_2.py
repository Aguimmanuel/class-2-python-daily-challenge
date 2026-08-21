
student_name = input("Student name: ")
mathematics_score =  float(input("Mathematics score: "))
english_score = float(input("English score: "))
basic_science_score = float(input("Basic Science score: "))

print(" ")
print("-" * 5 , "REPORT CARD" , "-" * 5)
print(f"Student: {student_name}")
print(f"Mathematics: {mathematics_score}")
print(f"English: {english_score}")
print(f"Basic Science: {basic_science_score}")
print(f"TOTAL: {(mathematics_score + english_score + basic_science_score):.2f}")
print(f"AVERAGE: {((mathematics_score + english_score + basic_science_score)/3):.2f}")