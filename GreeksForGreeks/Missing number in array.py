class Solution:
    def MissingNumber(self,array,n):
        l=[i for i in range(1,1+n)]
        return sum(l)-sum(array)

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
