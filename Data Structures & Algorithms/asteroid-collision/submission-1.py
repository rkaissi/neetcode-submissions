class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack) > 1:
                first, second = stack[-1], stack[-2]

                if first > 0 and second > 0 or first < 0 and second < 0 or first > 0 and second < 0:
                    break
                
                stack.pop()
                stack.pop()
                
                if abs(first) > abs(second):
                    stack.append(first)
                elif abs(first) < abs(second):
                    stack.append(second)

        return stack