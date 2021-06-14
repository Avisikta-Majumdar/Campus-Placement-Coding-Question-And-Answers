'''
One programming language has the following keywords that cannot be used as identifiers:



break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var



Write a program to find if the given word is a keyword or not



Input #1:



defer



Output:



defer is a keyword

Input #2:
While

Output:
while is not a keyword

'''


keyword_list=['break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var']
for i in range(int(input("Testcase:-"))):
    Input = input()
    print(Input+" is a keyword"  if Input in keyword_list else Input+" is not a keyword")
    
