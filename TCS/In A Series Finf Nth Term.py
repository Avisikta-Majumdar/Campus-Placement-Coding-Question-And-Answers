"""
This is a pattern
1 1 2 3 4 9 8 27 16 81 32 243 .....
This series is a mixture of 2 different series 1 is power of 2 series another 1 is
power of 3 series.
Write an algorithm to get the nth term of this series

Test Case1:-
Input:- 11
Output:-32

"""

def FindValue(n):
    if n&1:
        print(2**((n//2)))
    else:
        print(3**(n//2-1))
        


Input= int(input("Enter n:-"))
FindValue(Input)

"""
Logic :-
Checking the n value is odd or even if it's odd then it means it will be in power of 2 series
and the power will be n//2
If n is even this means the value will be power of 3 and the power will be n//2-1
-1 because the power is starting from 0 not 1
"""
