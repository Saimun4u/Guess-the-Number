import random
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

# *** SECOND SOLUTION ***

def guess(x):
    random_number = random.randint(1,x)
    guess = 0


