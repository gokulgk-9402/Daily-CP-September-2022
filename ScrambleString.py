class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        mem = {}
        
        def recursion(string1, string2):
            
            length = len(string1)

            if string1 == string2:
                return True
            elif mem.get((string1, string2), mem.get((string2, string1))) is not None:
                return mem.get(((string1, string2)), mem.get((string2, string1)))
            else:
                h1 = {}
                h2 = {}
                for i in range(1, length):
                    h2[string2[i - 1]] = h2.get(string2[i - 1], 0) + 1
                    h1[string1[i - 1]] = h1.get(string1[i - 1], 0) + 1
                    flag = True
                    for k in set([*h1.keys(), *h2.keys()]):
                        if h1.get(k, 0) != h2.get(k, 0):
                            flag = False

                    if flag:
                        f1 = recursion(string1[:i], string2[:i])
                        f2 = recursion(string1[i:], string2[i:])

                        if f1 and f2:
                            mem[(string1, string2)] = True
                            mem[(string2, string1)] = True
                            return True

                h1 = {}
                h2 = {}

                for i in range(1, length):
                    h2[string2[length - i]] = h2.get(string2[length - i], 0) + 1
                    h1[string1[i - 1]] = h1.get(string1[i - 1], 0) + 1
                    flag = True
                    for k in set([*h1.keys(), *h2.keys()]):
                        if h1.get(k, 0) != h2.get(k, 0):
                            flag = False

                    if flag:
                        f1 = recursion(string1[:i], string2[length - i:])
                        f2 = recursion(string1[i:], string2[:length - i])

                        if f1 and f2:
                            mem[(string1, string2)] = True
                            mem[(string2, string1)] = True
                            return True
            
            
            mem[(string1, string2)] = False
            mem[(string2, string1)] = False

            return False

        return recursion(s1, s2)

print(Solution().isScramble(s1 = "great", s2 = "rgeat"))