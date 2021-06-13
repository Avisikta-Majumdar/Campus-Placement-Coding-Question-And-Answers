class Solution:
    def ExtractNumber(self,S):
        s=[]
        S = S.split(" ")
        for i in S:
            if len(i)>0 and ord(i[0])>47 and ord(i[0])<57 and ("9" not in i):
                s.append(int(i))
        s.sort()
        
        return -1 if len(s)==0 else s[-1]
                    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends
