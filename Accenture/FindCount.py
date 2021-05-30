#Question
'''You are given a function FindCount
The function accpets an int array 'arr'
The function will return the no of elements of 'arr' having absolute difference
of less than or equal to 'diff' with ' num'''
#Input:-
'''arr: 12 3 14 56 77 13
   num:12
   diff:2
   '''
#Output : -
# 3 
def FindCount(array , length , num , diff):
    count = 0
    for i in array:
        if abs(i-num)<=diff:
            count+=1
    return -1 if count==0 else count  #Ternary Operator


Input = input("Enter the elements of array:- ")
num = int(input("num :-"))
diff = int(input("diff :- "))
Array = Input.split(" ")
array = [int(i) for i in Array]
print(FindCount(array , len(array) , num , diff))
