"""
Input will be a number(n)
Output will be sum of all the non- prime no.s present in n
Note :-  Consider 0 & 1 as prime no

Test Case 1 :-
Input:- 45673
Output:-10 (4+6) = 10 --> Because 4 & 6 are non prime digits in n

"""
Input=input("")
prime=[0,1,2,3,5,7]
total=0
for i in Input:
    if int(i) not in prime:
        total+=int(i)

print(total)
