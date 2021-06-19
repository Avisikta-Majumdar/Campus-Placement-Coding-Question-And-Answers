'''
Write a program to generate Fibonacci Series
'''
def Fibonacci(n):
    l=[0 , 1]
    a,b = 0,1
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        for i in range(3,1+n):
            a , b = b, a+b
            l.append(b)
    return l

for i in range(int(input("Test case:-"))):
    print(Fibonacci(int(input(""))))
