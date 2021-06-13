#User function Template for python3
import math
class Solution:
    def noOfOpenDoors(self, N):
        l=[]
        for i in range(1, N + 1):
            root_n = int(math.sqrt(i))
            
            if ((root_n * root_n) == i):
                
                print(root_n , i)
                l.append(1)
                continue
            else:
                l.append(0)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.noOfOpenDoors(N))
# } Driver Code Ends



#Logic:-
'''
Only square number will be open.
'''
