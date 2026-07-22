class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opMap = {"+": self.add, "-": self.sub, "*": self.mult, "/": self.div}

        for token in tokens:
            if token in opMap:
                second, first = stack.pop(), stack.pop()
                stack.append(opMap[token](first, second))
            else:
                stack.append(int(token))
        
        return stack[-1] if stack else 0
    
    def add(self, first, second):
        return first + second

    def sub(self, first, second):
        return first - second
    
    def mult(self, first, second):
        return first * second
    
    def div(self, first, second):
        return int(first / second)