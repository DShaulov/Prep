from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursiveGenParentheses("(", n, 1, 0)
    def recursiveGenParentheses(self, current: str, n:int, openers:int, closers:int) -> List[str]:
        # Stop condition - final string
        if openers == closers == n:
            return [current]
        # Case where there is no more room for openers
        elif openers == n:
            return self.recursiveGenParentheses(current + ")", n, openers, closers + 1)
        # Case where there is no more room for closers
        elif openers == closers:
            return self.recursiveGenParentheses(current + "(", n, openers + 1, closers)
        # Case where there is room for both openers and closers
        else:
            return self.recursiveGenParentheses(current + ")", n, openers, closers + 1) + self.recursiveGenParentheses(current + "(", n, openers + 1, closers)

sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))