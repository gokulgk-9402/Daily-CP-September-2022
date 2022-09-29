class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        index = bisect.bisect_right(arr, x)
        left = index - 1
        right = index
        
        curr = 0
        ans = []
        
        while curr < k:
            if left < 0:
                ans.append(arr[right])
                right += 1
                curr += 1
            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1
                curr += 1
            elif (abs(arr[left] - x) <= abs(arr[right] - x)):
                ans.append(arr[left])
                left -= 1
                curr += 1
            else:
                ans.append(arr[right])
                curr += 1
                right += 1
                
        ans.sort()
        return ans