#naming things
#version 2.0
'''
change:
multiply to subtract
fix bug when input is string and it's error, to loop the program
'''

import random

def add(x, y):
    return x + y

def subtract(x, y):#for future upgrade
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):#for future upgrade
    return x / y

print("choose the game.")
print("1.Add")
print("2.subtract")

#let's user choose
choice = input("Enter choice(1/2): ")


while True:
    try:
        #for addition
        if choice == "1":
            #random integer from 1-10
            a=random.randrange(1,10)
            b=random.randrange(1,10)
            print(a," + ", b)
            question=a+b
            answer=input("put your answer : ")
            #to break
            if answer == "break":
                break
            if question == int(answer):
                print("\tcorrect")
                print("")
            else:
                print("\twrong answer is :",question)
                print("")
    except:
        pass
    try:
        #for subtract
        if choice == "2":
            #random integer from 1-10
            a=random.randrange(1,10)
            b=random.randrange(1,10)
            print(a," - ", b)
            question=a-b
            answer=int(input("put your answer : "))
            #to break
            if answer == "break":
                break
            if question == answer:
                print("\tcorrect")
                print("")
            else:
                print("\twrong answer is :",question)
                print("")
    except:
        pass

input=("thank for playing the game")