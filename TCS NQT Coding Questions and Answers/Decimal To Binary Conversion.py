'''
Write a Python program which will convert a given decimal integer number N to its binary equivalent.
The given number N, a positive integer, will be passed to the program using the first command line parameter.
Print the equivalent binary number to stdout. Other than the binary number, no other extra information should be printed to stdout
Example:
Given input “19”, here N=19,
expected output 10011
'''

def DecToBinary(number):
    s=''
    #Method 1
    while number:
        r=number%2
        s+=str(r)
        number//=2
    return s[::-1]

for i in range(int(input("Testcase:-"))):
    print(DecToBinary(int(input(""))))
