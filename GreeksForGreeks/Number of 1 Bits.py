#User function Template for python3
class Solution:
	def setBits(self, N):
		BinaryN = bin(N)
		#print(BinaryN)
		BinaryN = str(BinaryN[2:])
		l=[int(i) for i in BinaryN]
		return sum(l)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)


