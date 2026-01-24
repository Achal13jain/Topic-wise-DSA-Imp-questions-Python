# Design a data structure that supports:
# insert(val)
# remove(val)
# getRandom()
# All in O(1) time.

# 🔹 Idea
# List for random access
# Hashmap for index tracking
# Swap with last element on delete

import random

class RandomizedSet:
    def __init__(self):
        self.arr = []      # stores values
        self.index = {}    # value → index

    def insert(self, val):
        if val in self.index:
            return False

        self.arr.append(val)
        self.index[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        if val not in self.index:
            return False

        # Get index of element to remove
        idx = self.index[val]
        last_val = self.arr[-1]

        # Swap with last element
        self.arr[idx] = last_val
        self.index[last_val] = idx

        # Remove last
        self.arr.pop()
        del self.index[val]

        return True

    def getRandom(self):
        # Random choice from array
        return self.arr[random.randint(0, len(self.arr) - 1)]
    
    
# Example usage:
random_set = RandomizedSet()
print(random_set.insert(1))    # True
print(random_set.insert(2))    # True
print(random_set.remove(1))    # True
print(random_set.getRandom())  # 2
print(random_set.insert(2))    # False
print(random_set.remove(3))    # False

# ⏱ Time: O(1) for all operations
# 📦 Space: O(n)