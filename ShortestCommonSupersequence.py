class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        mem = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(l1 -1, -1, -1):
            for j in range(l2 -1, -1, -1):
                if str1[i] == str2[j]:
                    mem[i][j] = 1 + mem[i+1][j+1]
                else:
                    mem[i][j] = max(mem[i+1][j], mem[i][j+1])

        ptr1 = 0
        ptr2 = 0

        lcs = ""
        lcs_len = mem[0][0]

        while ptr1 < l1 and ptr2 < l2:
            if str1[ptr1] == str2[ptr2]:
                lcs += str1[ptr1]
                ptr1 += 1
                ptr2 += 1

            else:
                e = mem[ptr1][ptr2 + 1]
                s = mem[ptr1 + 1][ptr2]
                if e > s:
                    ptr2 += 1
                else:
                    ptr1 += 1

        ans = ""
        ptr1 = 0
        ptr2 = 0
        ptr_lcs = 0

        while ptr1 < l1 and ptr2 < l2 and ptr_lcs < lcs_len:
            char1 = str1[ptr1]
            char2 = str2[ptr2]
            charlcs = lcs[ptr_lcs]

            if char1 == char2 and char2 == charlcs:
                ans += char1
                ptr1 += 1
                ptr2 += 1
                ptr_lcs += 1

            elif char1 == charlcs and char2 != charlcs:
                ans += char2
                ptr2 += 1

            elif char1 != charlcs and char2 == charlcs:
                ans += char1
                ptr1 += 1

            else:
                ans += (char1 + char2)
                ptr1 += 1
                ptr2 += 1

        while ptr1 < l1:
            ans += str1[ptr1]
            ptr1 += 1
        while ptr2 < l2:
            ans += str2[ptr2]
            ptr2 += 1

        return ans
 
print(Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab"))