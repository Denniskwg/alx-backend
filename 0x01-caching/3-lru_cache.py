#!/usr/bin/env python3
"""3-lru_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching
    """
    def __init__(self):
        """initializes an object from the class
        """
        BaseCaching.__init__(self)
        self.track = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.track:
                idx = self.track.index(key)
                del self.track[idx]
                self.track.insert(0, key)
            else:
                self.track = [key] + self.track

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            #items = sorted(self.track.items(), key=lambda item: item[1])
            #val = items[0][0]
            #del self.cache_data[val]
            #del self.track[val]
            val = self.track[BaseCaching.MAX_ITEMS]
            del self.cache_data[val]
            del self.track[BaseCaching.MAX_ITEMS]
            print("DISCARD: {}".format(val))

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if self.cache_data.get(key, None) is not None:
            idx = self.track.index(key)
            del self.track[idx]
            self.track = [key] + self.track
        return self.cache_data.get(key, None)
