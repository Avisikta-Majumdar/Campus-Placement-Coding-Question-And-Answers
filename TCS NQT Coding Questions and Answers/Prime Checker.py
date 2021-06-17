'''
C Program to check whether a given number is a prime number or not. The given number N,
a positive integer, will be passed to the program using the first command line parameter.
If it is a prime number the output should be the square root of the number up to 2 decimal point
precision, If it is not a prime number then print 0.00 to stdout
'''
def CheckPrimeOrNot(number):
    flag=0
    for i in range(2,number):
        if number%i==0:#Not prime number
            flag=1
            break

    return "0.00" if flag else round((number**.5),2)
    '''if flag:#no is not prime
        return "0.00"
    else:
        return round((number**.5),2)'''
        


for i in range(int(input("Testcase:-"))):
    number=int(input())
    print(CheckPrimeOrNot(number))
