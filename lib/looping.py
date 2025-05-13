#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list
    pass

def fizzbuzz():
    num = 1
    while num < 101:
        if (num % 3 == 0 and num % 5 == 0):
          print("FizzBuzz")
        elif (num % 5 == 0):
          print("Buzz")
        elif (num % 3 == 0):
          print("Fizz")
        else:
          print(num)    
        num += 1
    pass
