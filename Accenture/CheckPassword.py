#'Str' is a vaild password if it statisfied below conditions:
    #At least 4 characters
    #At least 1 numeric digits
    #At least 1 Capital letter
    #Must not have space or slash(/)
    #Starting Character must not be a no.

def CheckPassword(Str):
    num_digit=0
    char=0
    len=0
    CapsLetter= 0
    for i in range(len(Str)):
        if (i==0 and (ord(Str[i])>47 and ord(Str[0])<58)) or (Str[i]==" ") or (Str[i]=="/"):
            return 0 #3rd & 4th condition failed
        else:
            if (ord(Str[i])>64 and ord(Str[0])<91):
                CapsLetter+=1
                len+=1
                char+=1
                continue
            elif (ord(Str[i])>47 and ord(Str[0])<58):
                num_digit+=1
                len+=1
                continue
            else:
                char+=1
                len+=1
    if char>3 and CapsLetter>0 and num_digit>0 and len>3:
        return 1
    else:
        return 0


Password = input("Enter password :-")
print(CheckPassword(Password))

#input:- aA1_67
#output:-1
