#1) Write code to check a String is palindrome or not?

##A palindrome is those String whose reverse is equal to the original.
#Input :- madam
#Output:- True

String = input("")
print("This is a palindrome String" if String==String[::-1] else "This is not a palindrome String ")
