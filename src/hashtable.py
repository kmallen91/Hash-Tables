# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        # takes hash turns into index
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # hash key to make index
        index = self._hash_mod(key)
        # if hashed key already exists == collision
        if self.storage[index] is not None:
            print(f'Error: item at index {index}')
        else:
            # else add key value to hashed key location
            self.storage[index] = (key, value)
            return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash key
        index = self._hash_mod(key)
        old_item = None
        # if hash exists
        if self.storage[index] is not None:
            # and if is correct key
            if self.storage[index][0] == key:
                # set old item to be deleted value
                old_item = self.storage[index]
                # set to None
                self.storage[index] = None
            # if not correct key, collision
            else:
                print(f'Error: collision occurred at {index}')
        # else key doesn't exist
        else:
            print("Error: key not found ")
        # return deleted value
        return old_item

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash key
        index = self._hash_mod(key)
        # if hash exists
        if self.storage[index] is not None:
            # if key is correct hash
            if self.storage[index][0] == key:
                # return value at key
                return self.storage[index][1]
            else:
                print(f'Error: collision at index {index}')
        # if hash doesn't exist, return none
        else:
            return None

        return

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # set old storage in variable to iterate through
        old_storage = self.storage
        # update storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # iterate through old storage, inserting key, values into new storage
        for item in old_storage:
            if item is not None:
                self.insert(item[0], item[1])


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
