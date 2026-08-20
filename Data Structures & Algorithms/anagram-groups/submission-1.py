class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counts = {}
        for s in strs:
            arr = [0 for i in range(26)]
            for c in s:
                arr[ord(c) - ord('a')] += 1
            
            if tuple(arr) in counts:
                counts[tuple(arr)].append(s)
            else:
                counts[tuple(arr)] = [s]
        
        return list(counts.values())

