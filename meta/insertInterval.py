class Solution:
    def insert(self, intervals, newInterval):

        affected = [newInterval]
        leftRes = []
        rightRes = []

        def isOut(i,j,k,l):
            if i<k and j<k:
                return True
            if i>l and j>l:
                return True
            return False

        flag = False    


        for e in intervals:
            if isOut(e[0],e[1],newInterval[0],newInterval[1]):
                if e[0]<newInterval[0] and e[1]<newInterval[0]:
                    leftRes.append(e[0:])
                else:
                    rightRes.append(e[0:])

                 
            else:
               
                affected.append(e[0:])
        ##merging affected and sorting just affected not the whole array
        
        affected.sort()

        mergedAffected = []
        prev = None
        for e in affected:
            print (e)
            if prev==None:
                prev = e
            else:
                if prev[1]>=e[0]:
                    prev[1]=max(e[1],prev[1])

                else:
                    mergedAffected.append(prev)
                    prev=e
                 
        if prev:mergedAffected.append(prev)

        return leftRes+mergedAffected+rightRes

                            


             


        