# Accessing items
letters = ['a', 'b', 'c', 'd']
letters[0] = "A"
print(letters[0:])

# List unpacking
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 99]
first, second, *others, last = numbers
print(f"\n {first}, {second}")
print(others)
print(f"{last}\n")

#Looping over list
for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

#Adding or removing items
letters.append('e')
print(f"\n{letters}")
letters.insert(0, '-')
letters.remove('c')
print(f"{letters}\n")

#Finding items
print(letters.index("e"))
if "b" in letters:
    print(letters.index("b"))
print(letters.count("a"))

#Sorting list
numbers.sort(reverse=True)#sorting in desending order
print(f"\n{numbers}")

items = [
    ("Product_1", 156),
    ("Product_2", 145),
    ("Product_3", 269),
    ("Product_4", 26),
    ("Product_5", 173)
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(f"\n{items}")

#Lambda function(one line function you can pass to other function)
items = [
    ("Product_1", 156),
    ("Product_2", 145),
    ("Product_3", 269),
    ("Product_4", 26),
    ("Product_5", 173)
]

items.sort(key=lambda item:item[1])
print(f"\n{items}")

#Map & Filter function
maped = list(map(lambda item: item[1], items))
maped = [item[1] for item in items] #List comprehension 

filtered = list(filter(lambda item: item[1] <= 150, items))
print(filtered)
filtered = [item for item in items if item[1] <= 150] #List comprehension 

