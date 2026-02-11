'''
x = input("z: ")
print(type(x))

y = int(x) + 1
print(f"x: {x}, y: {y}")3
'''
# if, elif & else
temp = 30

if temp > 32:
    print("It's warm")
elif temp < 14:
    print("It's cool")
else:
    print("Perfect temp")
print("Done")

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)

# cleaner code
age = 17
status = "Eligible" if age >= 18 else "Not eligible "
print(status)

high_income = False
good_credit = True

if high_income and good_credit:
    print("Yes loan")
else:
    print("No")

student = False
if (high_income or good_credit) and not student:
    print("Accepted")
else:
    print("Denied")

# For loop
for number in range(5):
    print("Attempt", number + 1, (number + 1) * ".")
# clearner code
for number in range(1, 6):
    print("Execute", number, number * ".")

successful = False
for number in range(3):
    print("Tried")
    if successful:
        print("Complited")
        break
else:
    print("Attempt failed")

# Nested loop
for a in range(5):
    for b in range(3):
        print(f"({a}, {b})")

#interable
for d in "Python":
    print(d) 
for e in [1, 2, 3, 4, 5]:
    print(e)

# while loop
figure = 100
while figure > 0:
    print(figure)
    figure //= 2
'''
command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
'''
#infinite loops (run forever neeed to break)
while True:
    command = input(">")
    print("Echo", command)
    if command.upper() == "QUIT":
        break