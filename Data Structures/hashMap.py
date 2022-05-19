class HashMap:

    def __init__(self, size):
        self.size = size
        self.arr = [[] for i in range(size)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def __setitem__(self, key, value): # This handles collisions using Chaining
        h = self.getHash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
        if not found:
                self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.getHash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

theHash = HashMap(10)

theHash['boy'] = 13
theHash['girl'] = 15
theHash['Jack'] = 24
theHash['Jill'] = 30

print(theHash.arr)
