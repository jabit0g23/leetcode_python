class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        newS=""
        if n==1:
            return "1"
        s=self.countAndSay(n-1)
        newS=""
        cnt=1
        pointer=0
        length = len(s)
        while pointer <length:
            if pointer+1 <length and s[pointer] == s[pointer+1]:
                cnt+=1
                pointer+=1
            elif pointer+1 <length:
                newS+=str(cnt)+s[pointer]
                cnt=1
                pointer+=1
            else:
                newS+=str(cnt)+s[pointer]
                break
        s=newS
        return newS
        
