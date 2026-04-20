"""Read two integers from the user and display their sum."""


def main():
    """Run the program."""
    try:
        # Read the first number
        first_number = int(input("Enter the first number: "))

        # Read the second number
        second_number = int(input("Enter the second number: "))

        # Calculate the sum
        total_sum = first_number + second_number

        # Display the result
        print(f"Sum: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter whole numbers only.")


if __name__ == "__main__":
    main()