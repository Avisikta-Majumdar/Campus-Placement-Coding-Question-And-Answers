'''
Write a c program, to find the GCD of the given 2 numbers,
using command line arguments. The input is 2 integer and
the output GCD also should be an integer value.
'''

GCD=0
a,b = (int(input()) for i in range(2))
for i in range(1,1+min(a,b)):
    if a%i==0 and b%i==0:
        GCD=i
print("GCD of {} & {} is {}".format(a,b,GCD))
    
