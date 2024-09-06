def remove_uneven(numbers):
    uneven = []
    for number in numbers:
        if number % 2 == 0:
            uneven.append(number)
    return uneven

def main():
    original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even = remove_uneven(original_numbers)

    print(f"The original numbers are: {original_numbers}")
    print(f"The even numbers are: {even}")

if __name__ == "__main__":
    main()

