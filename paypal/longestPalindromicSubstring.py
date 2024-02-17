class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[ 0 for i in range(len(s))] for j in range(len(s))]
        ans = 1
        current = s[0]

        for gap in range(len(s)):
            i = 0
            j = gap
            while i<len(s) and j<len(s):
            
                if j-i+1==1:
                    dp[i][j] = 1
                elif j-i+1==2:
                    if s[i]==s[j]:
                        dp[i][j]=1
                    else:
                        dp[i][j]=0
                else:
                    if s[i]==s[j] and dp[i+1][j-1]==1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=0
                if dp[i][j]==1:
                    if j-i+1>ans:
                        ans =j-i+1
                        current=s[i:j+1]
                            
                i+=1
                j+=1

        return current


        