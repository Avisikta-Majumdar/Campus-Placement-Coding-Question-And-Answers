'''
Write a Python Program to check whether a given number is a strong number or not.
 The given number N, a positive integer, will be passed to the program
 using the first command line parameter.
 If it is a strong number, the output should be “YES”,
 If it is not a prime number then output should be “NO” to stdout.
 Other than YES or NO, no other extra information should be printed to stdout.

STRONG NUMBER:-Strong number is a special number whose sum of the factorial of digits is equal to the original number. For Example: 145 is strong number.
Example1:-
Input:-145
Output:-YES

 '''
def factorial(n):
    return n*factorial(n-1) if n>1 else 1

def CheckStrongNumber(number):
    no = number
    total=0
    while number>0:
        r = number%10
        total+=factorial(r)
        number//=10
    return "YES" if no==total else "NO"

for i in range(int(input("Testcases:-"))):
    print(CheckStrongNumber(int(input(""))))
    

