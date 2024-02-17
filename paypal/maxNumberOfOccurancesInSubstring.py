###Important question...

##brute force

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:


        hm = {}
        for i in range(len(s)):
            for j in range(i,min(len(s),i+26+1)):
                temp = s[i:j+1]
                if len(set(temp))<=maxLetters and j-i+1<=maxSize and j-i+1>=minSize:
                    if temp in hm:
                        hm[temp]+=1
                    else:
                        hm[temp]=1    
        maxy = 0
    
        for k in hm:
            maxy= max(maxy,hm[k])
        return maxy  
##-----optimized--------

## if a substring is present then its minimumsize substring shall also be there ..

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:


        hm = {}
        for i in range(len(s)):
            j = i+minSize-1
            temp = s[i:j+1]
            if len(set(temp))<=maxLetters:
                if temp in hm:
                    hm[temp]+=1
                else:
                    hm[temp]=1    
        maxy = 0
    
        for k in hm:
            maxy= max(maxy,hm[k])
        return maxy             