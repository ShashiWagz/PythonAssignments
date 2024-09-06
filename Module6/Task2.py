

def gallon_to_liter(gallons):
    liter= gallons * 3.7854
    return liter

def main ():
    while True:
        input_gallon=int(input("Enter the number of gallons: "))

        if input_gallon<0:
            print("Please Enter enter a positive number")
            break

        liter=gallon_to_liter(input_gallon)
        print(liter)
        break

if __name__ == '__main__':
    main()


