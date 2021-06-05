"""
You are playing an online game . In the game, a number is displayed on the screen.
In order to win the game , you have to Count the trailing zeros in the factorial value of the given no

Write an algorithm to count the trailing zeros in the factorial value of the given number.

Test Case 1:-
Input:-5
Output:- 1
Explanation:-

"""
import math
def TrailingZeros(number):
    fact = math.factorial(number)
    lst=[int(i) for i in str(fact)]
    #print(lst)
    return lst.count(0)

Input= int(input("Enter a number:-"))
print(TrailingZeros(Input))
