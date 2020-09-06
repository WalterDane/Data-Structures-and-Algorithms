class HashTable(): #type: abstract unordered associative array
    def __init__(self):
        self.buckets = [0] * 10007 #creates a list of 100007 (prime) pointers that point to 0

    def insert(self, key, value):
        """
        Inserts a key and its associated value
        Average: O(1)
        Worst Case: O(n)
        """
        index = index(key, self.len(buckets))
        self.buckets[index] = value

    def search(self, key):
        """
        Searches for the value for the given key
        Average: O(1)
        Worst Case: O(n)
        """
        index = index(key, self.len(buckets))
        value = self.buckets

    def index(self, key, bucket_size):
        """
        Finds the index given the key and bucket size
        Average: O(1)
        Worst Case: O(n)
        """
        if self.buckets[index] != 0:
            probe_counter = 0
            index = self.probe(key, bucket_size, probe_counter)
        else:    
            hash = hash(key)
            index = hash + % bucket_size
    
    def probe(key, bucket_size, probe_counter):
        """
        Use linear probing and probe recursively until an available index is found
        Average: O(1)
        Worst Case: O(n)
        """
        if probe_counter > 1:
            hash = hash(key)
            index = hash + probe_counter % bucket_size
            if self.buckets[index] != 0
                probe_counter+=1
                probe(key, bucket_size, probe_counter)
            else:
                index = hash + probe_counter % bucket_size
                return index
        probe_counter = 1
        probe(key, bucket_size, probe_counter)
    
    def chain(): #TO BE IMPLEMENTED
        """
        Use seperate chaining to handle collisions
        Average: O(1)
        Worst Case: O(n)
        """
        pass

    def hash(self, key):
        """
        Should be efficient computable and provide a uniform 
        distribution of hash values. Only handles strings and integers
        """
        hash = None
        if isinstance(key, str):
            for char in key:
                hash *= ord(char) #won't work well for anagram, so we need to check to see (later addition)
        else: 
            hash = key
        return hash

    def calcute_load_factor(self):
        """
        Calculates the load factor by finding n and then dividing
        n by k (the size of bucket)
        n - the number of entries occupied in the hash table
        k - the number of buckets
        """
        n = None
        k = len(self.buckets)
        for value in buckets:
            if value != 0 and n != None:
                n += 1
            if value != 0 and n == None:
                n = 1
        load_factor = n / k        
        return load_factor