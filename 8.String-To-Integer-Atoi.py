class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        return sign * result