#User function Template for python3
from collections import deque

class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
        #code here
        q = deque()

        for i in range(k):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)

        ans = []

        for i in range(k, n):
            ans.append(arr[q[0]])
            while q and q[0] <= i - k:
                q.popleft()

            while q and arr[i] >= arr[q[-1]]:
                q.pop()

            q.append(i)

        ans.append(arr[q[0]])

        return ans

arr = [int(x) for x in "1 2 3 1 4 5 2 3 6".split()]
print(Solution().max_of_subarrays(arr, 9, 3))