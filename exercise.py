# Write a program to display the even numbers between 1-10 after print "we have the 4 even number"
'''
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even number")
'''
# A dice rolling game
'''
import random

while True:
    choice = input("Roll the dice? (y/n): ")
    if choice.lower == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")
'''
# Number guessing game
'''
import random

number_to_guess = random.randint(1, 100)

while True:
    try:
    #user_input = input("Guess the number between 1 and 100: ")
    #guess = int(user_input)
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break    

    except ValueError:
        print(guess)
'''
# Rock paper scissors (r/p/s)
'''
import random

choices = ('r', 'p', 's')

while True:
    user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == "r" and computer_choice == Scissors) or
        (user_choice == "s" and computer_choice == Paper) or
        (user_choice == "p" and computer_choice == "r")):
        print("You win")
    else:
        print("You lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == "n":
        break

#Refactoring & modulization (dry)= dont repeat your self

import random

Rock = "r"
Paper = "p"
Scissors = "s"

choices = (Rock, Paper, Scissors)

def get_user_choices():
    while True:
        user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! ")

def display_choice(user_choice, computer_choice):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif(
        (user_choice == Rock and computer_choice == Scissors) or
        (user_choice == Scissors and computer_choice == Paper) or
        (user_choice == Paper and computer_choice == Rock)):
        print("You win")
    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choices()

        computer_choice = random.choice(choices)

        display_choice(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break
play_game()
'''

# Currency convertion
'''
while True:
    try:
        amount = float(input("Enter the amount "))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Invalid amount")

currencies = ('USD', 'EUR', 'CAD')

while True:
    source_currency = input("Source currency (USD/EUR/CAD): ").upper()
    if source_currency not in currencies:
        print("Invalid currency")
    else:
        break

while True:
    target_currency = input("Target currency (USD/EUR/CAD): ").upper()
    if target_currency not in currencies:
        print("Invalid currency")
    else:
        break

exchange_rate = {
    'USD': { 'EUR': 0.85, 'CAD': 1.25 },
    'EUR': { 'USD': 1.18, 'CAD': 1.47 },
    'CAD': { 'USD': 0.80, 'EUR': 0.68 },
}

if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * exchange_rate[source_currency][target_currency]
print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")


#continue (y/n)

currencies = ('USD', 'EUR', 'CAD')

exchange_rate = {
    'USD': {'EUR': 0.85, 'CAD': 1.25},
    'EUR': {'USD': 1.18, 'CAD': 1.47},
    'CAD': {'USD': 0.80, 'EUR': 0.68},
}

while True:
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Invalid amount")

    while True:
        source_currency = input("Source currency (USD/EUR/CAD): ").upper()
        if source_currency not in currencies:
            print("Invalid currency")
        else:
            break

    while True:
        target_currency = input("Target currency (USD/EUR/CAD): ").upper()
        if target_currency not in currencies:
            print("Invalid currency")
        else:
            break

    if source_currency == target_currency:
        converted_amount = amount
    else:
        converted_amount = amount * exchange_rate[source_currency][target_currency]

    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == "n":
        print("\nThank you for using the Currency Converter!")
        print("We hope you found it helpful. Have a great day! 🌟")
        break
'''

#Refactoring & modulization
'''
def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid amount")

def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f"{label} currency (USD/EUR/CAD): ").upper()
        if currency not in currencies:
            print("Invalid currency")
        else:
            return currency

def convert(amount, source_currency, target_currency):
    exchange_rate = {
        'USD': { 'EUR': 0.85, 'CAD': 1.25 },
        'EUR': { 'USD': 1.18, 'CAD': 1.47 },
        'CAD': { 'USD': 0.80, 'EUR': 0.68 },
    }

    if source_currency == target_currency:
        return amount
    
    return amount * exchange_rate[source_currency][target_currency]

def main():
    while True:
        amount = get_amount()
        source_currency = get_currency("Source")
        target_currency = get_currency("Target")
        converted_amount = convert(amount, source_currency, target_currency)
        print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            print("\nThank you for using the Currency Converter!")
            print("We hope you found it helpful. Have a great day! 🌟")
            break
        
if __name__ == "__main__":
    main()
'''
#Quiz game
'''
import random
from termcolor import cprint

quiz = [
    {
        "question": 'What is  the capital of France',
        "options": ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        "answer": 'C' 
    },
    {
        "question": 'Which planet is known as the red planet?',
        "options": ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        "answer": 'B' 
    },
    {
        "question": 'What is the largest ocean on Earth?',
        "options": ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
        "answer": 'D' 
    }
]

random.shuffle(quiz)

score = 0

for index, item in enumerate(quiz, 1):
    print(f"Question {index}: {item["question"]}")

    for option in item["options"]:
        print(option)

    answer = input("Your answer: ").upper().strip()

    if answer == item["answer"]:
        cprint("Correct!", "green")
        score += 1
    else:
        cprint(f"Wrong! The correct answer is {item["answer"]}", "red")

print(f"Quiz over! Your final score is {score} out of {len(quiz)}")
'''
#Refactoring & modulaization

import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

def ask_question(index, question, options):
  print(f'Question {index}: {question}')
  for option in options:
    print(option)

  return input('Your answer: ').upper().strip()  

def run_quiz(quiz):
  random.shuffle(quiz)

  score = 0

  for index, item in enumerate(quiz, 1):
    answer = ask_question(index, item[QUESTION], item[OPTIONS])

    if answer == item[ANSWER]:
      cprint('Correct!', 'green')
      score += 1
    else:
      cprint(f'Wrong! The correct answer is {item[ANSWER]}', 'red')

  print(f'Quiz over! Your final score is {score} out of {len(quiz)}')


def main():  
  quiz = [
    {
      QUESTION: 'What is the capital of France?',
      OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
      ANSWER: 'C'
    },
    {
      QUESTION: 'Which planet is known as the red planet?',
      OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
      ANSWER: 'B'
    },
    {
      QUESTION: 'What is the largest ocean on Earth?',
      OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
      ANSWER: 'D'
    }
  ]  
  run_quiz(quiz)

if __name__ == '__main__':
  main()
