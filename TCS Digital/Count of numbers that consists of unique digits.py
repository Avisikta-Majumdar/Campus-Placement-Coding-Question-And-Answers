'''
Q1. Write a program to find the count of numbers that consists of unique digits.



Input:

Input consists of two Integer lower and upper value of a range



Output:

The output consists of a single line, print the count of unique digits in a given range. Else Print"No Unique Number"



Solution:

Input -

10

15

Output -

5

'''
def Count(lower,upper):
    count=0
    for i in range(lower , 1+upper):
        flag=1
        s=str(i)
        s = [i for i in s]
        for i in s:
            if s.count(i)>1:
                flag=0
        if flag==1:
            count+=1
    return count if count>0 else "No Unique Number"




if __name__=="__main__":
    while True:
        n,m = (int(input()) for i in [1,2])
        print(Count(n,m))
