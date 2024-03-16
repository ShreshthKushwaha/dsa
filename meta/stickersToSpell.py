class Solution:
    def minStickers(self, stickers, target: str) -> int:


        stickers_count = []
        mem = {}
        for s in stickers:
            hm = {}
            for e in s:
                if e in hm:
                    hm[e]+=1
                else:
                    hm[e]=1
            stickers_count.append(hm)


        def find(targetWord):
            if targetWord in mem:
                return mem[targetWord]

            if targetWord=="":
                return 0
            mini = 2**31
            #making a hashmap of remaining target word
            target_hm={}
            for e in targetWord:
                if e in target_hm:
                    target_hm[e]+=1
                else:
                    target_hm[e]=1
            for s in stickers_count:
                if targetWord[0] not in s:
                    continue
                    
                remaining_words = {}
                for e in target_hm:
                    if e in s:
                        remaining_words[e]=max(0,target_hm[e]-s[e])
                    else:
                        remaining_words[e]=target_hm[e]

                newRemString = ""
                for k in remaining_words:
                    newRemString+=(remaining_words[k]*k)

                mini = min(1+find(newRemString),mini)
            mem[targetWord]=mini    
            return mini
        ans =  find(target)     
        if ans>=2**31:
            return -1
        return ans    
                                                 
        