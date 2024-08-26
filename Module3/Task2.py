#give options for user
print("Choose your cabin class : LUX  /  A   /  B  /  C  ")

#get input from user
userInput = input("Enter the cabin class of a cruise ship: ")

#check the conditions and print the output
if userInput == "LUX":
    print("upper-deck cabin with a balcony.")
elif userInput == "A":
    print("above the car deck, equipped with a window.")
elif userInput == "B":
    print(" windowless cabin above the car deck.")
elif userInput == "C":
    print(" windowless cabin below the car deck.")

else:
    print("The cabin class you entered is invalid.")
