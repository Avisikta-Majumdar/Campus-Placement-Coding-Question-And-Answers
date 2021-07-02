'''
Q2. There is a range given n and m in which we have to find the count of all the prime pairs whose difference is 6. We have to find how many sets are there within a given range.



Output:

The output consists of a single line, print the count prime pairs in a given range. Else print"No Prime Pairs".



Constraints:

2<=n<=1000

n<=m<=2000



Sample Input:

4

30



Output:

6

Explanation:

(5, 11) (7, 13) (11, 17) (13, 19) (17, 23) (23, 29) . we have 6 prime pairs.


Input -

101

500

Output:-
30

'''
def Prime(i):
    if i == 1:
        return 0
    else:
        for ij in range(2,i):
            if i%ij==0:
                return 0
        return 1


def Count(lower , upper):
    prime=[]
    count=0
    for i in range(lower,1+upper):
        if Prime(i):
            prime.append(i)

    for i in prime:
        for j in prime:
            if abs(i-j)==6:
                count+=1
    return count//2 if count//2>0 else "No Prime Pairs"




if __name__=='__main__':
    while True:
        n , m = (int(input()) for i in [1,2])
        print(Count(n,m))
