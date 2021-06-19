'''
Write a C program to find whether the given number is an Armstrong number or not using command line arguments.
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number
since 3**3 + 7**3 + 1**3 = 371.
'''

def Armstrong(n):
    l = len(str(n))
    store = n
    r=0
    total=0
    while n:
       r=n%10
       total += (r**l)
       n//=10
    return total == store


for i in range(int(input("Test cases:- "))):
    no = int(input())
    print("Armstrong no" if Armstrong(no) else "Not Armstrong no")
