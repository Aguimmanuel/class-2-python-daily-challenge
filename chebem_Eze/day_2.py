name = input("Student name: ")

math_score = float(input("Mathematics score: "))

english_score = float(input("English score: "))
basic_science_score = float(input("Basic Science: "))
total = math_score + english_score + basic_science_score
average = total/3

print("----- REPORT CARD -----")
print(f"Student: {name}")
print(f"Mathematics: {math_score}")
print(f"English: {english_score}")
print(f"Mathematics: {basic_science_score}")
print(f"TOTAL: {total:.2f}")
print(f"AVERAGE: {average:.2f}")
print("-------------------------")
