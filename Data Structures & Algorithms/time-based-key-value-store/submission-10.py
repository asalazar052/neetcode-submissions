class TimeMap:

    def __init__(self):
        self.contents = {} # checks if the value exists in the first place
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.contents:
            self.contents[key] = [] 
    
        self.contents[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.contents:
            return ""
        
        arr = self.contents[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1 # we want to see if there is anything closer to timestamp worth finding
            else:
                r = m - 1 # we need a smaller value than the current m
        
        return res

        
'''

Get MUST return the most recent value of 'key' given that 'set' was previously called on it
AND the most recent timestamp is less than or equal to the given timestamp

Note: if there's no value for key that is less than the given timestamp, return ""

'''