""" This program helps NIN Enrollment officer do their jobs effectively """

age_valid, id_card_valid, consent_valid = False, False, False
while True:
    if not age_valid:
        age = int(input("Age: "))
        if 18<= age <=110:
            age_valid = True
        else:
            continue
    if not id_card_valid:
        id_card = input("Means of ID (passport / voter / licence / national): ")
        if id_card== "passport" or id_card== "voter" or id_card== "license" or id_card== "national":
            id_card_valid = True
        else:
            continue
    if not consent_valid:
        consent = input("Consent to enrol (yes/no): ")
        if consent == "yes" or consent == "no":
            consent_valid = True
        else:
            continue
    if age_valid and id_card_valid and consent_valid:
        break

if consent == "yes":
    message = f"ENROLLED - age {age}, ID {id_card}, consent yes"
elif consent == "no":
    message = f"DECLINED - consent no"

print(message)
