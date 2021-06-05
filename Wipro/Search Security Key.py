"""
Find the security key
as input we will give an integer ,your task is to find how many no are repeated .
Test case 1 :-
Input:- 578378923
Output:- 3
Explanation:- The repeated digits in the data are 7,8,3. So, the security key is 3.
"""
def SecurityKey(number):
    l=[]
    for i in str(number):
        l.append(int(i))
    securityKey=0
    for i in l:
        if l.count(i)>1:
            securityKey+=1
            l.remove(i)
    return securityKey if securityKey>0 else -1

Input = int(input("Enter no :-"))
print(SecurityKey(Input))
