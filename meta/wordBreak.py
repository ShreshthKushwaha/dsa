class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        mem = {}
        def make(k):
            if k==len(s):
                return True
            if k>len(s):
                return False
            if k in mem:
                return mem[k]    
            result = False
            for e in wordDict:

                if len(e)+k<=len(s):
                    
                    if s[k:k+len(e)]==e:
                        
                        result = result or make(k+len(e))
            mem[k]=result            
            return result
        return make(0)  