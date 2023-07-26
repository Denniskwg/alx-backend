#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple
"""1-simple_pagination defines a class Server with methods
dataset and get_page
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """return a tuple of size two containing a start
        index and an end index corresponding to the range
        of indexes to return in a list for those particular
        pagination parameters.
        """
        return ((page - 1) * page_size, page_size * page)

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
        """returns a sub list containing data from a pagination
        algorithm index_range which returns the indexes to
        start pagination on the list. If input arguments are out of range
        for the dataset, an empty list is be returned.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        indexes = self.index_range(page, page_size)
        data = self.dataset()
        if indexes[0] > (len(data) - page_size):
            return []
        else:
            lst = data[indexes[0]:indexes[1]]
            return lst
