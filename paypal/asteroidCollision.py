class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for e in asteroids:
            if stack==[]:
                stack.append(e)
            elif e<0<stack[-1]:
                f = 0
                while len(stack)>0 and e<0<stack[-1]:
                    popped = stack.pop()
                    if abs(e)<abs(popped):
                        stack.append(popped)
                        f = 1
                        break
                    elif abs(e)==abs(popped):
                        f = 1
                        break
                      
                if f==0:
                    stack.append(e)
            else:
                stack.append(e)
        return stack                         


           