while True:
    age = int(input("Age: "))
    if age >=18 and age <= 110:
        break

while True:
    id = input("Means of ID (passport / voter / licence / national): ")
    if id == "passport" or id == "voter" or id == "licence" or id == "national":
        break

while True:
    consent = input("Consent to enrol (yes/no): ")
    if consent == "yes" or consent == "no":
        break

if consent == "yes":
    print(f"ENROLLED - age {age}, ID {id}, consent {consent}")
else:
    print("ENROLLMENT DECLINED - consent not given")