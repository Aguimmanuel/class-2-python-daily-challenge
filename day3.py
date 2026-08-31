
name = input("input your name: ")
score = int(input("input your score: "))
print()
remain_score = 100 - score

if score < 0 or score >100:
    print("invalid score")
elif score >= 70 and score <= 100:
    print(f"{name} scored {score}: A (Excellent)")


elif score >= 60 and score <= 69:
    remain_score = 70 - score

    print(f"{name} scored {score}:  B (Very good) \n{remain_score} more marks to reach A")

elif score >= 50 and score <= 59:
    remain_score = 60 - score
    print(f"{name} scored {score}: C (Good)\n {remain_score} more marks to reach B")
elif score >= 45 and score <= 49:
    remain_score = 50 - score
    print(f"{name} scored {score}: D (Pass) \n{remain_score} more marks to reach C")
elif score >= 0 and score <= 44:
    remain_score = 45 - score

    print(f"{name} scored {score}: F (Fail)\n {remain_score} more marks to reach D")
else:
    print("invalid input")
