Valid_username="python"
Valid_password="rules"

attempts=0

while attempts<5:
    username=str(input("Please Enter Username:"))
    password=str(input("Please Enter Password:"))

    if username == Valid_username and password== Valid_password:
        print("Welcome")
        break
    elif username != Valid_username and password != Valid_password:
        print("Invalid Username or Password, Please enter the username and password again")
    attempts += 1

if attempts == 5:
    print("Access Denied")




