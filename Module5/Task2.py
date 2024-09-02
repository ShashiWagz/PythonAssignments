
numbers = []

while True:
    userInput = input("Enter a number (or press Enter to finish): ")

    if userInput == "":
        break

    try:

        number = float(userInput)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")


numbers.sort(reverse=True)


print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)
