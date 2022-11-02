import random
number = random.randint(1, 100)
guess = int(input("What is your guess for the secret number? "))
tries = 0 
while guess != number:
    if guess > number:
        print(f'{guess} is too high')
    else:
        print(f'{guess} is too low')
    guess = int(input('What is your next guess? '))
    tries = tries + 1
tries = tries + 1
print(f"On guess number {tries}, you guessed the secret number {number}!")
