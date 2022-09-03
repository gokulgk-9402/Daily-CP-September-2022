from typing import List

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        s = list(s)
        stack = []

        total = s.count(letter)
        count = 0

        for index, i in enumerate(s):
            while stack and stack[-1] > i:
                if stack[-1] == letter and i != letter:
                    if total + count - 1 < repetition:
                        break

                if len(stack) + len(s) - index - 1 < k:
                    break

                if stack[-1] == letter:
                    count -= 1

                stack.pop()

            stack.append(i)
            if i == letter:
                count += 1
                total -= 1
        
        temp = 0
        while len(stack) + temp > k:
            if stack[-1] == letter and count <= repetition:
                temp += 1
            if stack[-1] == letter:
                count -= 1

            stack.pop()

        return "".join(stack) + temp * letter

print(Solution().smallestSubsequence(s = "leetcode", k = 4, letter = "e", repetition = 2))
