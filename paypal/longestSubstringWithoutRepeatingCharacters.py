class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mem_index = {}

        i = 0

        ans = 0
        for j in range(len(s)):
            ##agar repeating hai toh dictionary mai se i se last_index tak ke sare element hata do
            if s[j] in mem_index and mem_index[s[j]]!=-1:
                last_index = mem_index[s[j]]
                for ii in range(i,last_index+1):
                    mem_index[s[ii]]=-1
                i=last_index+1
            mem_index[s[j]]=j
            ans = max(ans,j-i+1)
        return ans
#-----optimized

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mem_index = {}

        i = 0

        ans = 0
        for j in range(len(s)):
            ##agar repeating hai toh dictionary mai se i se last_index tak ke sare element hata do
            if s[j] in mem_index and mem_index[s[j]]!=-1:
                last_index = mem_index[s[j]]
                if i<=last_index:
                    i=last_index+1
            mem_index[s[j]]=j
            ans = max(ans,j-i+1)
        return ans        

           


      

        