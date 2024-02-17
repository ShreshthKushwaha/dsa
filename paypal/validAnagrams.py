#----brute----
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if "".join(sorted(list(s)))=="".join(sorted(list(t))):
            return True
        return False   
#----better-----
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alph = [0]*26
        for e in s:
            alph[ord(e)-98]+=1
        for e in t:
            alph[ord(e)-98]-=1
        for e in alph:
            if e!=0:
                return False
        return True           