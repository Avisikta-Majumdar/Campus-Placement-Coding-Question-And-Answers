#Write a method which will remove any given character from a String?

#Input :- madam      d
#Output:- maam


String = input("")
char = input("")
s=''
for i in String:
    if i!=char:
        s+=i
print(s)
