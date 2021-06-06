"""
Test Case1 :-
Input :-
4
(3,2,0,1)
Output:-
(3,2,1,0)


Test Case 2 :-
Input:- 7
(2,0,1,0,2,3,0)
Output:-
(2,1,2,3,0,0,0)
"""
def MoveZeros(array):
    #Method1
    for i in array:
        if i==0:
            array.remove(0)
            array.append(0)


    #Method 2
    """
    for index , value in enumerate(array):
        for i in range(index,len(array)-1):
            if array[i]==0:
                array[i] , array[1+i] = array[i+1] , array[i]
    """
    return array

    

Input = input("Enter elements of this array:-")
Input = [int(i) for i in Input.split(" ")]
print(MoveZeros(Input))
