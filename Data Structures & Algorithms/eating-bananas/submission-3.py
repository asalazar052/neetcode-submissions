class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r

        while l <= r: #?
            k = (r + l) // 2
            count = 0
            
            for p in piles:
                count += math.ceil(p/k)
                if count > h: # k is too small. Look for bigger k
                    l = k + 1
                    break

            if count <= h:
                # k is good, but there may be better (smaller k)
                res = k
                r = k - 1
            

        return res


    '''
    1 - 25
    13

    h -> num hours to eat all bananas
    k -> bananas per hour
    goal: return lowest k | finish all bananas in under h

    - observation: h has to be at least len(piles)

    try: testing all possible k's
    lowest k: 1
    highest k: max of piles (since anything higher than that would be redundant)
    '''