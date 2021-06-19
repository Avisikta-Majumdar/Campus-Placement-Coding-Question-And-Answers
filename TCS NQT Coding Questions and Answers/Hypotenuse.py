'''
Write a Python program to find the hypotenuse of a triangle using command line arguments
'''

def Hypotenuse(a,b):
    return ((a**2 + b**2))**.5


for i in range(int(input(""))):
    a , b =(int(input()) for i in [1,2])
    print(Hypotenuse(a,b))
