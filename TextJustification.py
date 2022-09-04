from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        n = len(words)
        
        def recursion(start):

            nonlocal n
            # print(start)
            if start >= n:
                return 
                
            curr = len(words[start])
            number = 0
            length = len(words[start])
            
            i = start + 1
            while i< n and curr + 1 + len(words[i]) <= maxWidth:
                # print(curr, maxWidth, words[i])
                curr += len(words[i]) + 1
                length += len(words[i])
                number += 1
                i += 1
            
            spaces = maxWidth - length
            left = number
            
            line = ""
            j = start
            
            if i == n:
                line = " ".join(words[j:i])
                line += " " * (maxWidth - len(line))
                ans.append(line)
                return

            while j < i:
                # print(words[j])
                line += words[j]
                if left != 0:
                    temp = 0
                    if spaces%left:
                        temp = 1
                    line += (spaces//left + temp)*" "
                    spaces -= (spaces//left + temp)
                else:
                    line += spaces * " "
                j += 1
                left -= 1
                
            ans.append(line)
            recursion(i)
            
        recursion(0)
        return ans

print(Solution().fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))