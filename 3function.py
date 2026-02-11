'''
# Defining function
def greet():
    print("Hi there")
    print("Welcome to function in python")


greet()


def great(first_name, last_name):
    print(f"Hi {first_name} {last_name} welcome")


great("Mosh", "Hamedani")

# increment


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# simplified code


def increment(number, by):
    return number + by


print(increment(3, 2))

# function for variable number of argument


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print("Start")
print(multiply(5, 4, 3, 2, 1))
'''
def fizzbuzz():
    number = int(input("Enter a number: "))

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Fizz"
    elif number % 3 == 0:
        return "Buzz"
    else:
        return number  # Return as string for consistency

print(fizzbuzz())  # This ensures output is shown

def fizzbuzz():
    while True:
        number = int(input("Enter a number: "))

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Fizz")
        elif number % 3 == 0:
            print("Buzz")
        else:
            print(number)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break

fizzbuzz()
