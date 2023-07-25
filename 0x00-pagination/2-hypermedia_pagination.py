#!/usr/bin/env python3
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range
"""1-simple_pagination defines a class Server with methods dataset
get_page and get_hyper
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a sub list from a pagination
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        data = self.dataset()
        if indexes[0] > (len(data) - page_size):
            return []
        else:
            lst = data[indexes[0]:indexes[1]]
            return lst

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dict with HATEOAS
        """
        if len(self.get_page(page, page_size)) == 0:
            next_page = None
            size = 0
        else:
            next_page = page + 1
            size = page_size
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        my_dict = {
            "page_size": size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }

        return my_dict
