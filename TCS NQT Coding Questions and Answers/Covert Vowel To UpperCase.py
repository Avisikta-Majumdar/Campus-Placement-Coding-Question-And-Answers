'''
Write a Python program to convert the vowels to an uppercase in a given string using command line arguments.
Example: if the input is tata, then the expected output is tAtA.
'''
def tataTotAtA(s):
    a={"a":"A" , "e":'E' , 'i':'I' , 'o':'O' , 'u':'U'}
    ss=''
    for i in s:
        if i in a.keys():
            ss+=a[i]
        else:
            ss+=i
    return ss


for i in range(int(input("Test case :-"))):
    string = input()
    print(tataTotAtA(string))
