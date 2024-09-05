class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append("".join(s))
                return
             
            if open_count < n:
                s.append('(')
                backtrack(s, open_count + 1, close_count)
                s.pop()
            
            if close_count < open_count:
                s.append(')')
                backtrack(s, open_count, close_count + 1)
                s.pop()
        
        result = []
        backtrack([], 0, 0) 
        return result
