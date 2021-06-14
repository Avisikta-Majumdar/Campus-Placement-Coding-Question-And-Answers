'''Given a maximum of four digit to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G)
as input, output its decimal value.

Input:

23GF



Output:
10980


'''


def ConvertHexToDec(number):
    d={"A":10,"B":11,"C":12,"D":13, "E":14, "F":15 , "G":16}
    total , count = 0,0
    for i in number[::-1]:
        if i in d.keys():
            total+= (int(d[i])*(17**count))
            count+=1
        else:
            total+= (int(i) * (17**count))
            count+=1
    return total



for i in range(int(input("TestCase:-"))):
    number = input()
    print(ConvertHexToDec(number))
