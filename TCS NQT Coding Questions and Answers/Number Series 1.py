'''
TCS Coding question – 1
Consider the following series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187…
This series is a mixture of 2 series – all the odd terms in this series
form a geometric series and all the even terms form yet another geometric series.
Write a program to find the Nth term in the series.

The value N is a positive integer that should be read from STDIN. The Nth term that is calculated by the program should be written to STDOUT. Other than the value of the nth term, no other character/string or message should be written to STDOUT. For example, if N=16, the 16th term in the series is 2187, so only value 2187 should be printed to STDOUT.
You can assume that N will not exceed 30.

Input: 16
Output: 2187

'''

def NthTerm(n):
    '''
    METHOD 1 
    result=0
    res2=1
    res3=1
    for i in range(3,1+n):
        if i&1:#Series of 2
            res2*=2
            result=res2
            
        else:#series of 3
            res3*= 3
            result=res3
    return result'''
    #Method 2
    if n&1:
        return 2**(n//2)
    else:
        return 3**(n//2-1)

n=int(input())
print(NthTerm(n) if n<=30 else "N value must be in between 1 to 30")
