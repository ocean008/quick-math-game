#naming things
#version 1.0

from multiprocessing.resource_sharer import stop
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
print("2.multiply")

#let's user choose
choice = input("Enter choice(1/2): ")


while True:
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

    #for multiplication
    if choice == "2":
        #random integer from 1-10
        a=random.randrange(1,10)
        b=random.randrange(1,10)
        print(a," x ", b)
        question=a*b
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

input=("thank for playing the game")