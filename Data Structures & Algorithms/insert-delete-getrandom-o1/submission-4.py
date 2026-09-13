import random

class RandomizedSet:

    def __init__(self):
        
        self.vals = []
        self.indicies = {} # Value : Index


    def insert(self, val: int) -> bool:
        # Return false if item was present
        if val in self.indicies:
            return False
        
        self.indicies[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Return true if item was present, false otherwise
        if val not in self.indicies:
            return False

        # Swap current idx with the element at the end
        idx = self.indicies[val]
        self.vals[idx] = self.vals[-1]
        self.indicies[self.vals[idx]] = idx

        # Remove all record of it
        self.vals.pop()
        self.indicies.pop(val)
        
        return True

    def getRandom(self) -> int:

        
        return random.choice(self.vals)

        

'''
[1,4,3,4]

temp = 2

2 : 1
4 : 3
'''


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()