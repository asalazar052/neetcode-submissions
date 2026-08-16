import random

class RandomizedSet:

    def __init__(self):

        self.myDict = dict() # Value, index in the list
        self.myList = []
        

    def insert(self, val: int) -> bool:
        
        if val in self.myDict:
            return False
        
        self.myDict[val] = len(self.myList)
        self.myList.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.myDict:
            return False
        
        idx = self.myDict[val]
        swapper = self.myList[-1]
        self.myList[idx] = swapper
        self.myDict[swapper] = idx
        self.myList.pop()
        self.myDict.pop(val)

        return True

    def getRandom(self) -> int:

        return random.choice(self.myList)
        
'''
{2: 0, 1: 1}

[2, 1]

idx = 0

'''

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()