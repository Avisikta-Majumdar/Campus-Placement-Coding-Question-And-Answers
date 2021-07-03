'''
Write a program to print all the combinations of the given word with or without meaning (when unique characters are given).



Sample Input:

abc



Output:

abc

acb

bac

bca

cba

cab



Solution:

Input -

hai

Output:-
hai
hia
aih
ahi
iah
iha
'''



from itertools import permutations

letters = input()

# size of permutations is set to 3
a = permutations(letters, len(letters))
y = [''.join(i) for i in a]
for i in y:
    print(i)


