'''
Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits.

Input 1:
4567

Expected output: 
2



Explanation
The Sum of odd position digits 4 and 6 is 10.
The Sum of even position digits 5 and 7 is 12.
The difference is 12-10=2.



Input #2: 
9834698765123

Output:
1
'''

oddPositionSum , evenPositionSum = 0,0
for i in range(int(input("Testcase:-"))):
    number = input()
    for index, value in enumerate(number):
        if index&1:#Odd Position
            oddPositionSum+= int(value)
        else:
            evenPositionSum+= int(value)
    print(abs(oddPositionSum - evenPositionSum))
        
    
