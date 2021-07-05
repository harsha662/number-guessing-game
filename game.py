import random
number = random.randint(1,9)
#word = input("enter your number")
c = 0
while c<5:
    guess = int (input("enter your number"))
    if(guess==number):
        print("congratulation you won")
    elif guess<number:
        print("your guess is too low guess the higher number",guess)
    else:
        print("your guess was too high,guess a no lower than ",guess)
    c = c+1
if(c==5):
    print("you loose and the number is",number)

