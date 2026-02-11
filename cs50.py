num = 1 + 4
print(num, "it is", type(num))

name = input("What's your name? ")
color = input("What's your favorite color? ")
print (name + " likes " + color)

Patient_name = "John Smith"
Age = 20
New = True

if Patient_name == "John Smith" and Age == 20:
    print("He is a new pateint")
else:
    print("He is not a new pateint")

Birth_year = input("What's your birth year? ")
Current_age = 2026 - int(Birth_year)

print(Current_age)

weight_kgs = input("Enter your weight in kgs: ")
weight_pounds = float(weight_kgs) * 2.2
print(weight_pounds, "lbs")