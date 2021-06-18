'''
Write a Python program to check whether the given number is a perfect square or not using command line arguments.
'''
for i in range(int(input("Test cases:-"))):
    n=int(input(""))
    for i in range(n):
        if i**2==n:
            print("Yes")
            break
    if i==n-1:
        print("No")
