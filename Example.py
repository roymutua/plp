numbers = []

userInput = int(input("How many values are you entering "))

for i in range(userInput):
    value = int(input("Enter the value "))
    numbers.append(value)

total = sum(numbers)

print(f'List of values:, {numbers}\n sum of values:, {total}')
