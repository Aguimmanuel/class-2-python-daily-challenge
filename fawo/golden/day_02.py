student_name = input("Student name: ")
math = float(input("Mathematics Score: "))
english = float(input("English Score: "))
basic_science = float(input("Basic Science: "))

total = math + english + basic_science
average = total / 3

print("------Report Card-------")
print(f"Student: {student_name}")
print(f"Mathematics: {math}")
print(f"English: {english}")
print(f"Basic Science: {basic_science}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")