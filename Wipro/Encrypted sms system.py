#Wipro Coding Question
#Input :- 1st line it will take a no and in 2nd line it will take a string

#Output:- It will return a string where each characters' ascii value will be increased by input no. 

no = int(input())
st = input()
s=""
for i in st:
    temp = ord(i) + 3
    s+= chr(temp)
    
print(s)



#Test case 1:
#Input :- 3
#       as3gAsd
#Output:-
#       dv6jDvg


