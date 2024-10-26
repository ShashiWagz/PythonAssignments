airports={}

icao_codes=set()

while True:
    print("")
    print(".............OPTIONS.............")
    print("01.ENTER A NEW AIRPORT")
    print("02.FETCHING INFORMATION")
    print("03.QUIT")
    print("")
    choice=input("Enter your choice (01/02/03))   :  ")

    if choice== '01':
        icao=input("Please enter the icao code of the airport : ")

        if icao in icao_codes:
            print("The airport with icao code {icao} is already exist as {airport[icao][1]}")

        else:
            airport_name=input("Enter the name of the airport -  ")
            airport_info=(icao,airport_name)
            airports[icao]=airport_info
            icao_codes.add(icao)
            print(f"Airport {airport_name} with ICAO code {icao} has been added.")
            print("")
            print("")

    elif choice == '02':

        icao = input("Enter the ICAO code of the airport you want to fetch: ")

        if icao in icao_codes:
            print(f"The airport with ICAO code {icao} is {airports[icao][1]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")
            print("")
            print("")

    elif choice == '03':
            print("Goodbye!")
            break

    else:
        print("Invalid choice. Please choose 01, 02, or 03......")






