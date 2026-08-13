class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        temp = defaultdict(int)
        for i in s:
            temp[i]+=1

        for i in t:
            if i not in t:
                return False
            temp[i]-=1
            if temp[i] < 0:
                return False
        
        return True
