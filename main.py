import random
# num = random.randint(1,10)
# print(num)

def guess_number():
    num = random.randint(1,5)
    guess = int(input('Guess the number: '))
    while True:
      if guess != num:
          print('Your guess is wrong🤣 Better luck next time')
          res = input("Do you want to try again - Yes-y, No-n ")
          if res == "y":
             guess = int(input('Guess the number: '))
          elif res == "n":
             break
      else:
        print("Congratulations😊! You've guessed the correct number")
        res = input("Do you want to try again - Yes-y, No-n ")
        if res == "y":
           guess_number()
        elif res == "n":
           print('*****See you soon*****!')
           break

guess_number()