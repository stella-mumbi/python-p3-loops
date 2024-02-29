#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:  # Fix the loop condition to include 1
        print(i)
        i -= 1
    print("Happy New Year!")






def square_integers(int_list):
    return [x ** 2 for x in int_list]

# Example usage:
result = square_integers([1, 2, 3, 4, 5])
print(result)


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# Example usage:
fizzbuzz()
