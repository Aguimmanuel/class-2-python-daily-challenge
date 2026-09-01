name = input("Student name: ")

mathematics = float(input("Mathematics score: "))
english = float(input("English score: "))
basic_science = float(input("Basic Science score: "))

total = mathematics + english + basic_science
average = total / 3

print("\n----- REPORT CARD -----")
print(f"Student: {name}")
print(f"Mathematics: {mathematics}")
print(f"English: {english}")
print(f"Basic Science: {basic_science}")
print(f"TOTAL: {total:.2f}")
print(f"AVERAGE: {average:.2f}")