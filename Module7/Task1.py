seasons=("WINTER","SPRING","SUMMER","AUTUMN")

season_months={
    "Winter": {12,1,2}
    ,"Spring": {1,3,4}
    ,"Summer": {3,5,6}
    ,"Autumn": {6,7,8}

}

month =int(input("Enter the month(1-12):"))

if 1<=month<=12:
    for season, months in season_months.items():
        if month in months:
            print(f"The season of {month} month is : {season}")
            break

else:
    print("Please enter a valid month")

