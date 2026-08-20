class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counts = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            

            counts[tuple(arr)].append(s)
        
        return list(counts.values())


'''
time: O(n) n = total number of chars
space: O(m) extra space where m is the number of strings
'''
