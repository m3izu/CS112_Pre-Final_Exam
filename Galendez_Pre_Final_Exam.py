def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):
    # Function to display all prime numbers within a given range
    if start < 0:
        print("Enter a non-negative number.")
        return

    if end <= start:
        print("Enter a number greater than", start)
        return

    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    # Main program
    while True:
        start = int(input("Enter the start number: "))

        if start == 0:
            print("Program terminated.")
            break

        end = int(input("Enter the end number: "))

        # Display prime numbers within the specified range
        display_primes(start, end)
