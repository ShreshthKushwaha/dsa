class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}

        arr = sentence.split()
        res=[]
        i =1
        for e in arr:
            temp = e
            if e[0] in vowels:
                temp =temp+"ma"
            else:
                temp = temp[1:]+temp[0]+"ma"
            temp+=("a"*i)
            i+=1
            res.append(temp)
        return " ".join(res)      



        

        