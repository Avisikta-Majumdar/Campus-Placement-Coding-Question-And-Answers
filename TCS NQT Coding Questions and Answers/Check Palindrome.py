'''
Write a Python program to
check whether the given number is Palindrome or not using command line arguments.
'''
def PalinDrome(n):
    return n==n[::-1]

for i in range(int(input("Test case:-"))):
    print(PalinDrome(input()))
