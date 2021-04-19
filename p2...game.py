import random
num= random.randint(1,4)
for i in range(3):
    guess= int(input("Guess the Number: "))
    if guess== num:
        print("Congrats!! You are right")
        print("The number is: ",num)
        break
    elif guess<num:
        print("Guess a Bigger Number: ")
    else:
        print("Guess a Smaller Number: ")
else:
    print("Better Luck Next Time")
    print("The Number is: ",num)
