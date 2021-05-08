
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right. 



import random

# This means you are allowing your Python program to use a module called random in the rest of your code.

# To use it (and generate a random integer), now type:

# a = random.randrange(10)
# print(a)

#my solution

# a = random.randrange(10)
# b = input ("Guess a number between 1 and 9: ")
# if (a == b):
#     print("You are correct. The number is", a)
# else:
#     print("I am sorry",b,"is not correct. The correct number is: ",a)

# does not quite work

a = random.randint(1,9)
# a = 3
b = int(input ("Guess a number between 1 and 9: "))
if (a == b):
    print("You are correct. The number is", a)
else:
    print("I am sorry",b,"is not correct. The correct number is: ",a)

# does not quite work. 

# other solutions

# number = random.randint(1,9)
# random changes number every time. if you want to make sure the "you got it" comes up at the right time, 
# uncomment out the "number = 3 line"
# number = 3
# guess = 0
# count = 0

# this keeps game going until user types exit

# while guess != number and guess != "exit":
# the commented out code would be used for counting guesses or exiting
#however kept getting a loop error so not using these for now

# guess = int(input("What's your guess? "))

# guess = int(guess)
# count += 1

# if (guess < number):
#     print ("Too low")
# elif (guess > number):
#     print ("Too high")
# else:
#     print("You got it !")
    # print("It only took you ", count, "tries!")

# if guess == "exit": 
#     breakpoint



