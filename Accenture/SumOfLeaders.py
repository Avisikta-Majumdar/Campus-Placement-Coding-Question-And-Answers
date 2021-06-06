"""
The function accepts a positive integer array 'arr' of size 'n' as its argument.
Implement the function to find the leaders in the array and return their sum.

An element is leader in the array if it is greater than
all the elements to its right side.
The rightmost element is is always a leader .

Test case :-
Input:-  arr:52 66 64 36 45 24 32
Output:-207
Explanation:- Leaders of array are {66,64,45,32} Sum = 207
"""
def SumOfLeaders(array,n):
    Sum=0
    for index , value in enumerate(array):
        if max(array[index:])==value: #Checking the condition
          #  print(value,array[index:])
            Sum+=value
    return Sum
        


Input = input("Enter the elements of tyhe array:-")
Input = [int(i) for i in Input.split(" ")]

print("Sum Of Leaders:- " , SumOfLeaders(Input,len(Input)))


"""
Logic:-
In the function SumOfLeaders in if condion we are putting this condition
max(array[index:])==value
here it will take all the right side elements of this array with that element
after that checking the maximum value with that element
Example when for index , value in enumerate(array) index is 1 and value is 66 then
array[index:] will be [66,64,36,45,24,32] & max of this will be 66
then the condition will be true

"""


