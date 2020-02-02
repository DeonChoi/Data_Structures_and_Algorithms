class HashMap():
    def __init__(self, length = 256):
        #hashmap list/array of size 256
        self.hashmap = [None] * length

    #hash function using ASCII values
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % len(self.hashmap)

    #hash function using python's built in hash function
    def get_hash(self, key):
        hash_key = hash(key) % len(self.hashmap)
        return hash_key

    def add(self, key, value):
        key_hash = self._get_hash(key)
        # key_hash = self.get_hash(key)
        key_value = [key, value]

        #if bucket is empty, add to hashmap at that index, a list of new key_value pair
        if self.hashmap[key_hash] is None:
            self.hashmap[key_hash] = list([key_value])
            return True
        #if bucket is not empty
        else:
            for pair in self.hashmap[key_hash]:
                #if key already exists, then just update the value
                if pair[0] == key:
                    pair[1] = value
                    return True
            #if key doesnt already exist, we can append the key_value pair to that bucket
            self.hashmap[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        # key_hash = self.get_hash(key)

        #check if the bucket is not empty
        if self.hashmap[key_hash] is not None:
            #if bucket isnt empty, iterate through the key_value pairs in that bucket
            for pair in self.hashmap[key_hash]:
                #if the key matches the parameter 'key' then, we return the corresponding value of that key
                if pair[0] == key:
                    return pair[1]
        #if the key is not found, return None
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        # key_hash = self.get_hash(key)

        # check if bucket is empty. If it is, it means the key value pair does not exist, so we return False.
        if self.hashmap[key_hash] is None:
            return False
        #iterate through contents of that bucket. We use 'i in range' because we need the index, in order to use the .pop(i) to delete
        for i in range (0, len(self.hashmap[key_hash])):
            if self.hashmap[key_hash][i][0] == key:
                self.hashmap[key_hash].pop(i)
                return True

    def print(self):
        #iterates through buckets in hashmap, and prints out every non-empty bucket
        for item in self.hashmap:
            if item is not None:
                print(str(item))
    
    def is_empty(self):
        for item in self.hashmap:
            if item is not None:
                return False
        return True

hash_map = HashMap()

hash_map.add('Hello', 'Bye')
hash_map.add(1, 2)
hash_map.add('43141', 4142)
print(hash_map._get_hash('Hello'))
print(hash_map.get_hash('Hello'))

hash_map.print()
print(hash_map.is_empty())