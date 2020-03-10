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
            # create new node
            new_node = LinkedPair(key, value)
            # set current head to next node
            new_node.next = self.storage[index]
            # set index to new node
            self.storage[index] = new_node
        else:
            # else add key value to hashed key location
            self.storage[index] = LinkedPair(key, value)
            return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash key
        index = self._hash_mod(key)
        current_node = self.storage[index]
        # if key at head of LL, set current value to next item in LL
        if current_node.key == key:
            self.storage[index] = current_node.next

        # if not key at head of LL, traverse list
        if current_node.key != key:
            # while next node still exists
            while current_node.next is not None:
                # set prev node before moving
                prev_node = current_node
                # move forward
                current_node = current_node.next
                if current_node.key == key:
                    # if match, set prev node.next to skip current node
                    prev_node.next = current_node.next
                    return None
            print("Error: key not found ")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash key
        index = self._hash_mod(key)
        current_node = self.storage[index]

        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node.value

        if current_node.key != key:
            # loop while next value
            while current_node.next != None:
                # move value to next
                current_node = current_node.next
                # if found, return value
                if current_node == key:
                    return current_node.value
            return None

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
