'''
0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
This series is a mixture of 2 series all the odd terms in this series form even numbers
in ascending order and every even term is derived from the previous term using the
formula (x/2).
Write a program to find the nth term in this series.
The value n is a positive integer that should be read from STDIN the nth term that is calculated by
the program should be written to STDOUT. Other than the value of the nth term no other characters /strings or message should be written to STDOUT.

For example,
if n=10, the 10 th term in the series is to be derived from the 9th term in the series.
The 9th term is 8 so the 10th term is (8/2)=4. Only the value 4 should be printed to STDOUT.
You can assume that the ‘n’ will not exceed 20,000.
'''
def FindN1(n):#Method 1
    if n&1:#N is odd
        return 2*(int(n//2))
    else:#n is even
        return int((n-2)//2)



def FindN2(n):#Method 2
    lst=[0,0]
    odd=0
    even=0
    for i in range(3,1+n):
        if i&1:#i is odd
            odd+=2
            lst.append(odd)
        else:#i is even
            even+=1
            lst.append(even)
    print(lst)
    return lst[-1]
            
        


n=int(input())
print(FindN1(n) if n<20000 else "‘n’ will not exceed 20,000.")
print(FindN2(n) if n<20000 else "‘n’ will not exceed 20,000.")
