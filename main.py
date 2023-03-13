import random

# *** SECOND SOLUTION ***

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Guess is low')
        elif guess > random_number:
            print('Sorry, guess again. Guess is high') 
    
    print(f"Congratulations! You've guess the number {random_number} correctly!!!")

# guess(10)

# num = random.randint(1,10)
# print(num)

# *** FIRST SOLUTION ***

# def guess_number():
#     num = random.randint(1,5)
#     guess = int(input('Guess the number the computer generated between 1 and 5: '))
#     while True:
#       if guess != num:
#           print('Your guess is wrong🤣 Better luck next time')
#           res = input("Do you want to try again - Yes-y, No-n ")
#           if res == "y":
#              guess = int(input('Guess the number: '))
#           elif res == "n":
#              break
#       else:
#         print("Congratulations😊! You've guessed the correct number")
#         res = input("Do you want to try again - Yes-y, No-n ")
#         if res == "y":
#            guess_number()
#         elif res == "n":
#            print('*****See you soon*****!')
#            break

# guess_number()

# ********** A NEW PROGRAM TO HAVE THE COMPUTER GUESS THE SECRET NUMBER *********

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low!=high:
            guess =  random.randint(low,high)
        else:
            guess = low # could also be high as low can be equal to high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(1000)