'''
Calculate length of hypotenuse of right-angled triangle. 
'''

def Hypotenuse(a,b):
    return ((a**2 + b**2))**.5



for i in range(int(input("Test case :-"))):
    a , b =( int(input()) for i in [1,2])
    print(Hypotenuse(a,b))
