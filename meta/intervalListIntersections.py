class Solution:
    def intervalIntersection(self, firstList, secondList):

        firstList.sort()
        secondList.sort()
        ans = []

        def find(a,b,c,d):
            if c<=b and c>=a:
                return [c,min(b,d)]
            elif a>=c and a<=d:
                return [a,min(b,d)]
            else:
                return []


            

# ---        
# -----
#
#
        for a,b in firstList:
            for c,d in secondList:
                if find(a,b,c,d)!=[]:
                    ans.append(find(a,b,c,d))
        return ans            









        