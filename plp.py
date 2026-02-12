
#assignment week1
value1 = input(" Input the first number")
value2 = input(" Input the second number")

print(float(value1) + float(value2))


#assignment week 2
# Question 1
numbers = []

userInput = int(input("How many values are you entering "))

for i in range(userInput):
    value = int(input("Enter the value "))
    numbers.append(value)

total = sum(numbers)

print(f'List of values:, {numbers}\n sum of values:, {total}')


#Question 2
Books = ("The Trap", "Revenge", "Betrayal", "Cold cases")

for book in Books:
    print(book)


#Question 3
personInformation = {}

personInformation['Name'] = input("Your name ")
personInformation['Age'] = int(input("Your age "))
personInformation['Favourite colour'] = input("Your height ")

print("information: ", personInformation)


#Question 4
userSet1 = int(input("Enter the number of first set "))

for i in range(userSet1):
    number = int(input("Enter the set of integers "))

userSet2 = int(input("Enter the number of second set "))
for i in range(userSet2):
    number = int(input("Enter the set of integers "))

common = userSet1 & userSet2

print(f'First set: {userSet1}\n Second set: {userSet2}')
print(f'Common set: {common}')


#Question 5
listOfWords = ['Apple', 'Chair', 'Tabletop', 'Mouse', 'Keyboard']

oddWords = [ words for words in listOfWords if len(listOfWords) % 2 != 0 ]

print(f'Original words: {listOfWords}\n Odd number words: {oddWords}')
