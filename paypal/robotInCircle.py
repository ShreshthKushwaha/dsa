class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
##interviewer ko prove karna hai ki agar repeat hona hoga toh 4thi baar baad kar jayega repeat
        x,y = 0,0
        d = 1

        for i in instructions*4:
            if i=="G":
                if d==1:
                    y+=1
                elif d==2:
                    x+=1
                elif d==3:
                    y-=1
                elif d==0:
                    x-=1
            elif i=="L":
                d = (d-1)%4
            elif i=="R":
                d = (d+1)%4
        #if we are not running loop for 4 times then agar hum origin par wapas aajate hn toh wo wapas hi aate rahega....
        #ya phir agar direction change kar rha h ..iskamatlab wapas ussi direction m aayega agle baar toh uska matlab wo circle chlte rhega kyuki distance to same travel kr rha h har dirxn m
                                
        #if (x==0 and y==0)or d!=1:
        #    return True
        #return False  
        if x==0 and y==0 and d==1:
            return True
        return False    





        