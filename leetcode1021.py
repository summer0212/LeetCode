class Solution:
    def removeOuterParentheses(self, s) :
        final_str = []
        balance = 0

        for i in range(0,len(s)):
            if s[i] == '(':
                if balance > 0 :
                    final_str.append(s[i])
                    balance += 1
            elif s[i] == ')':
                balance -= 1
                


            
            
        