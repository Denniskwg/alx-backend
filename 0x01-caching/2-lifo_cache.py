#!/usr/bin/env python3
"""2-lifo_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching
    """
    def __init__(self):
        """initializes an object from the class
        """
        BaseCaching.__init__(self)
        self.track = {}
        self.number = 0

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        """
        if key is not None and item is not None:
            self.number = self.number + 1
            self.cache_data[key] = item
            self.track[self.number] = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            index = self.number - 1
            val = self.track[index]
            del self.cache_data[val]
            print("DISCARD: {}".format(val))

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
