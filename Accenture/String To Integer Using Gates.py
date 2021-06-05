"""
This function Result will accept a string and return a integer value
In this string consists of binary digits separated with an alphabet as follows:
  'A' denotes AND operation
  'B' denotes OR operaation
  'C' denotes XOR operation
scan the string left to right , taking operation at a time .

If string is NULL or None then return -1
"""


"""
Input:-1C0C1C1A0B1
Output:-1
"""
def Result(string):
    r=0
    if string==None:
        return -1
    else:
        while len(string)>2:
            print(string)
            s=string[0:3]
            if s[1]=="A":
                r = int(s[0]) & int(s[2])
            elif s[1]=='B':
                r= int(s[0]) | int(s[2])

            elif s[1]=='C':
                r = int(s[0]) ^ int(s[2])
                
            string = str(r) + string[3:] if len(string)>2 else str(r)
            #Using ternary operator the above condition will set string equals to r if
            #the length of the string is less than 2( it will hapeen only last time when the while loop will execute)
            #Otherwise it will add result with left string(which will calculated now).
            
        return r
    

Input = input("")
print("Result :- ",Result("1C0C1C1A0B1"))
