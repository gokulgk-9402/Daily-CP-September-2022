class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        number = len(flowers)
        flowers.sort()
        
        if flowers[0] >= target:
            return number*full
        
        pre = [0]
        lacking = [0]

        for flower in flowers:
            pre.append(pre[-1] + flower)

        count = 0
        for flower in flowers[::-1]:
            if flower >= target:
                count += 1
            lacking.append(lacking[-1] + max(target - flower, 0))

        def helper(flower, f, k):
            i = bisect.bisect_left(flowers, flower, lo=0, hi=k)
            return pre[i] + f >= i * flower

        ans = 0
        for k in range(count, number):
            if lacking[k] < newFlowers:
                left, right = flowers[0], target + 1
                while left < right:
                    mid = (left + right)//2
                    if not helper(mid, newFlowers-lacking[k], number-k):
                        right = mid
                    else:
                        left = mid + 1

                left -= 1

                if left >= target:
                    ans = max(ans, (target-1)*partial + k * full)
                else:
                    ans = max(ans, k*full + left*partial)

        if lacking[-1] <= newFlowers:
            ans = max(ans, number* full)

        return ans
        