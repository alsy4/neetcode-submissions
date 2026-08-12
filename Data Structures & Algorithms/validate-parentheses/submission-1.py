class Solution:
    def isValid(self, s: str) -> bool:
        """
        - Can do 2 pointer but use I'll chose to use stack
        - Hashmap{opening:closing}
        - For each c in s
        - Add the element to the stack
        - if element in the stack is in HashMap, pop
        - 
        
        """
        stack = []
        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in pair.values():
                stack.append(c)
            else:
                if stack and stack[-1] == pair.get(c):
                    stack.pop()
                else:
                    return False

        return True if not stack else False