"""
QUESTION
Given a sorted array of size N and an integer K,
find the position at which K is present in the array using binary search.
Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.


"""




#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
	    for index , value in enumerate(arr):
	        if value == k:
	            return index
	    return -1
		

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends
