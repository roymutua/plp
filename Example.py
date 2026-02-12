userSet1 = int(input("Enter the number of first set "))

for i in range(userSet1):
    number = int(input("Enter the set of integers "))

userSet2 = int(input("Enter the number of second set "))
for i in range(userSet2):
    number = int(input("Enter the set of integers "))

common = userSet1 & userSet2

print(f'First set: {userSet1}\n Second set: {userSet2}')
print(f'Common set: {common}')