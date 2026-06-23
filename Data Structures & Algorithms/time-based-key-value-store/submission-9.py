class TimeMap:

    def __init__(self):
        self.contents = {} # checks if the value exists in the first place
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.contents:
            self.contents[key] = [""] * 1001
        
        if timestamp <= 1000:
            self.contents[key][timestamp] = value

        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.contents:
            return ""
        
        arr = self.contents[key]
        for i in range(timestamp, -1, -1):
            if i <= 1000 and arr[i] != "":
                return arr[i]
        
        return ""
        

        
'''

Get MUST return the most recent value of 'key' given that 'set' was previously called on it
AND the most recent timestamp is less than or equal to the given timestamp

Note: if there's no value for key that is less than the given timestamp, return ""

'''