class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace(" ","")
        sign = 1
        result = 0
        number = 0
        stack = []


        for e in s:
            if e.isdigit():
                number=(10*number)+int(e)

            elif e=="+":
                result+=(sign*number)
                sign=+1
                number = 0
            elif e=="-":
                result+=(sign*number)
                sign=-1    
                number = 0
            elif e=="(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
                number = 0
            elif e==")":
                result+=(sign*number)
                number= 0
                prevSign = 1
                prevResult = 0

                if len(stack)>0:
                    prevSign = stack.pop()
                if len(stack)>0:    
                    prevResult = stack.pop()
                result=(result*prevSign)+prevResult
        
        if number!=0:
            result+=(sign*number) 
            number = 0       
        return result            




        