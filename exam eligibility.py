medical_reason = input("Was your absence caused by medical issues? Do you have any medical related problems that may effect your education? (Answer with Y or N):   ")
attendance = int(input(" How many days were you present in school?:  "))

if medical_reason == "Y":
    print("You may enter!")
else:
    if attendance >= 75:
        print("You may enter!")
    else:
        print("Request for entering was denied.")
