'''
Problem statement:

It was one of the places, where people need to get their provisions only through fair price (“ration”) shops. As the elder had domestic and official work to attend to, their wards were asked to buy the items from these shops. Needless to say, there was a long queue of boys and girls. To minimize the tedium of standing in the serpentine queue, the kids were given mints. I went to the last boy in the queue and asked him how many mints he has. He said that the number of mints he has is one less than the sum of all the mints of kids standing before him in the queue. So I went to the penultimate kid to know how many mints she has.



She said that if I add all the mints of kids before her and subtract one from it, the result equals the mints she has. It seemed to be a uniform response from everyone. So, I went to the boy at the head of the queue consoling myself that he would not give the same response as others. He said, “I have four mints”.

Given the number of first kid’s mints (n) and the length (len) of the queue as input, write a program to display the total number of mints with all the kids.

constraints:

2<n<10

1<len<20

Input#1:
4 2

Output:
7
Explanation:-
1st kid will have 4 mints
2nd kid will have 3 mints
No of total mints:- 4+3 = 7

Input#2:
14 4

Output:
105
Explanation:-
1st kid will have 14 mints
2nd kid will have 14-1 = 13 mints
3rd kid will have (14+13)-1 = 26 mints
4th kid will have(14+13+26)-1 = 52 mints

Total no of mints:- 14+13+26+52 = 105

'''

def NoOfTotalMints(n,length):
    total,mint=n ,n
    mint_lst=[n]
    for i in range(1, length):
        mint = sum(mint_lst)-1
        mint_lst.append(mint)
        #print(i , mint , mint_lst) For understanding purpose
    return sum(mint_lst)

Input=input("")
n,length = (int(i) for i in Input.split(" "))
print(NoOfTotalMints(n,length))
        

