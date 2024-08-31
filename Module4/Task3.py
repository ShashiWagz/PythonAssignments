smallest_number=0
largest_number=0

while True:
    userInput = input("Enter a number : ")

    if userInput == "":
        break

    number = int(userInput)

    if smallest_number == 0 or number < smallest_number:
        smallest_number = number

    if largest_number ==0 or number > largest_number:
        largest_number = number

if smallest_number !=0 and largest_number !=0:
    print(f"The smallest number is: {smallest_number}")
    print(f"The largest number is: {largest_number}")

