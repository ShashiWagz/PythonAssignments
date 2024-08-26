Gender=input("Enter your Gender: ")
hemoglobinLevel=float(input("Enter your hemoglobin level(g/l): "))


if Gender=="Male":
    if 134 <= hemoglobinLevel <= 167:
        print("Your hemoglobin Level is normal... ")
    elif hemoglobinLevel < 134 :
        print("Your hemoglobin Level is Low... ")
    elif hemoglobinLevel > 167:
        print("Your hemoglobin Level is High... ")
    else:
        print("The hemoglobin Level value is invalid")

elif Gender=="Female":
    if 117 <= hemoglobinLevel <= 155:
        print("Your hemoglobin Level is normal... ")
    elif hemoglobinLevel < 117:
        print("Your hemoglobin Level is Low... ")
    elif hemoglobinLevel > 155:
        print("Your hemoglobin Level is High... ")
    else:
        print("The hemoglobin Level value is invalid")

else:
    print("Please enter a valid Biological Gender")





