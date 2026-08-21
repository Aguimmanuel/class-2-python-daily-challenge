
student = input("Student name: ").title()
maths_score = float(input("Mathematics score: "))
english_score = float(input("English score: "))
basic_science_score = float(input("Basic Science score: "))
total_score = maths_score + english_score + basic_science_score
average = total_score/3
print()
print("------ REPORT CARD -------")
print(f"Student: {student}\nMathematics: {maths_score:.2f}\nEnglish: {english_score:.2f}")
print(f"Basic Science: {basic_science_score:.2f}\nTOTAL: {total_score:.2f}\nAVERAGE: {average:.2f}")