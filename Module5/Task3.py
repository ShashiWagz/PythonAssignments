user_input = int(input("Enter a number: "))

prime_num= True

if user_input > 1:
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            prime_num = False
            break

else:
    prime_num = False

if prime_num:
    print(user_input, "is a prime number")
else:
    print(user_input, "is not a prime number")


