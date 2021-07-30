for ii in range(int(input())):
    s=input("")
    s=[i for i in s.split(" ")]
    lst=[]
    for i in s:
        if ord(i[0])>47 and ord(i[0])<58 and "9" not in i:
            lst.append(int(i))
    lst.sort()
    print(lst[-1])