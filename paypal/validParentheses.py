class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for e in s:
            if e=="(":
                stack.append("(")
            elif e=="{":
                stack.append("{")
            elif e=="[":
                stack.append("[")
            else:
                if e==")":
                    if len(stack)==0 or stack[-1]!="(":
                        return False
                    else:
                        stack.pop()    

                elif e=="}":
                    if len(stack)==0 or stack[-1]!="{":
                        return False
                    else:
                        stack.pop()    

                elif e=="]":
                    if len(stack)==0 or stack[-1]!="[":
                        return False
                    else:
                        stack.pop()    
        if len(stack)>0:
            return False
        return True