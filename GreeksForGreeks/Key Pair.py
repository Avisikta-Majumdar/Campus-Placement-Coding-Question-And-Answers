#User function Template for python3
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		for value in (arr):
		    remaining = x-value
		   # arr.remove(value)
		    if remaining in arr and remaining!=value:
		        #print(value,remaining)
		        return 1
		    if remaining==value and arr.count(value)>1:
		        return 1
		return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1
