#!/usr/bin/env python3
"""1-fifo_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching
    """
    def __init__(self):
        """initializes an object from the class
        """
        BaseCaching.__init__(self)
        self.track = {}
        self.number = 0
        self.count = 0

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        """
        if key is not None and item is not None:
            self.number = self.number + 1
            self.cache_data[key] = item
            self.track[self.number] = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.count = self.count + 1
            val = self.track[self.count]
            del self.cache_data[val]
            print("DISCARD: {}".format(val))

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
