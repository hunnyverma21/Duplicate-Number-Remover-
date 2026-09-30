def remove_duplicates(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


def main():
    print("\n===== DUPLICATE NUMBER REMOVER =====")

    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [int(number) for number in user_input.split()]

        if not numbers:
            print("Please enter at least one number.")
            return

        unique_numbers = remove_duplicates(numbers)
        removed = len(numbers) - len(unique_numbers)

        print("\n===== RESULT =====")
        print("Original Numbers :", numbers)
        print("Unique Numbers   :", unique_numbers)
        print("Duplicates Removed:", removed)

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()
