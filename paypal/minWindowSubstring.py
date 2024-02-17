class Solution:
    def minWindow(self, s: str, t: str) -> str:

        inputHM ={}
        currentHM = {}

        for e in t:
            if e in inputHM:
                inputHM[e]+=1
            else:
                inputHM[e]=1
            currentHM[e]=0    
        j = 0
        i = 0
        matchCount = 0
        l = 2**31
        ans = ""
        while j<len(s):
            if s[j] in inputHM:
                if currentHM[s[j]]<inputHM[s[j]]:
                    matchCount+=1
                currentHM[s[j]]+=1
                while matchCount==len(t):
                    if (j-i+1)<l:
                        ans = s[i:j+1]
                        l = j-i+1
                    if s[i] in inputHM:
                        if currentHM[s[i]]==inputHM[s[i]]:
                            matchCount-=1
                        currentHM[s[i]]-=1 
                    i+=1  
            j+=1
        return ans       



        