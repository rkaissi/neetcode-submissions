class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            print(stack)            
            curr = 0
            if t == "+":
                curr = stack[-2] + stack[-1]
            elif t == "-":
                curr = stack[-2] - stack[-1]
            elif t == "*":
                curr = stack[-2] * stack[-1]
            elif t == "/":
                curr = int(float(stack[-2]) / stack[-1])
            else:
                stack.append(int(t))
                continue
            stack.pop()
            stack.pop()
            stack.append(curr)
        print(stack)
        return stack[-1]
                