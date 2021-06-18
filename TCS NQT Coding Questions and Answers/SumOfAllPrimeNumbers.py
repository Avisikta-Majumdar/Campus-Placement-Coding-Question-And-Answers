'''
Write a Python program that will find the sum of all prime numbers in a given range.
The range will be specified as command line parameters. The first command line parameter,
N1 which is a positive integer, will contain the lower bound of the range.
The second command line parameter N2, which is also a positive integer will contain the upper bound of the range.
The program should consider all the prime numbers within the range, excluding the upper bound and lower bound.
Print the output in integer format to stdout. Other than the integer number, no other extra information should be printed to stdout.
Example:-
Given inputs “7” and “24” here N1= 7 and N2=24,
expected output as 83.
'''
def Prime(n):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    return flag

def SumOfAllPrimeNumbers(lower,upper):
    total=0

    for i in range(lower+1,1+upper):
        if Prime(i):
            #print(i)
            total+=i
    return total


for i in range(int(input("Test cases:-"))):
    n1 , n2 = (int(input()) for i in [1,2])
    print(SumOfAllPrimeNumbers(n1 , n2))
