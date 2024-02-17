class Solution:
    def numberToWords(self, num: int) -> str:

        teen= {11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        tens = {0:"",1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
        ones = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
        d = {0:"",1:"Thousand",2:"Million",3:"Billion"}

        def spellHundred(n):
            if n//100>0:
                s = ones[n//100]
                n = n%100
                return s+" "+"Hundred"+" "+spellHundred(n)
            elif n//10>0:
                if n==10:
                    return "Ten"
                if n>10 and n<20:
                    return teen[n]    
                return tens[n//10]+" "+spellHundred(n%10)
            else:
                return ones[n]
        def spell(n):
            ans =""
            s = ""
            arr = []
            i = 0
            while n!=0:
                tempHundred= spellHundred(n%1000)
                if tempHundred!="":
                    arr.append(tempHundred+" "+d[i])
                i+=1
                n=n//1000
            print (arr)    
            for i in range(len(arr)-1,-1,-1):
                ans+=(arr[i]+" ")
             
            return ans   
        ans =  spell(num).strip()   
        if ans=="":
            return "Zero"
        return ans.replace("  "," ")   




                

         


        