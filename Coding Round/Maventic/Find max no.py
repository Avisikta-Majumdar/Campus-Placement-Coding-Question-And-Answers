s=input("")

l=[]
for i in range(len(s)-2):
    st = s[i:i+3]
    l.append(int(st))
print(max(l))
