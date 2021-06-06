"""
Implement the SumOfPro function
The function Takes 2 integer arrays 'aarr1' &'arr2' of size n as its argument. Implement the functyion to find the product of elements
of arr1 &arr2 by multiplying the first element of arr1 with the last element of arr2 .
second element of arr1 with the second last element of arr2 & so on.
i.e. (arr1[0]*arr2[n-1]) , (arr1[1] * arr2[n-2]),....
and return their sum of all the products obtained.


NOTE:-
if both array are empty return -1

TestCase1:-
Input:-
arr1:- 22 7 1 -5 5 -2
arr2:- 4 -1 21 12 10 -3

Output:- -102


"""
def SumOfPro(arr1 , arr2):
    Product=0
    arr2.reverse()
    if arr1==None and arr2==None :
        return -1
    else:
        for value1 , value2 in zip(arr1, arr2):
            Product += (value1 * value2)
        return Product

Array1 = input("Enter elements of array1:- ")
Array1 = [int(i) for i in Array1.split(" ")]

Array2 = input("Enter elements of array2:- ")
Array2 = [int(i) for i in Array2.split(" ")]

print(SumOfPro(Array1 , Array2))
