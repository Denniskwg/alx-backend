#!/usr/bin/env python3
BaseCaching = __import__('base_caching').BaseCaching
"""0-basic_cache
"""


class BasicCache(BaseCaching):
    def __init__(self):
        """initializes the BasicCache class object
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
