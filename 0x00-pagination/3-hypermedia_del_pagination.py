#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns a dictionary containing the next_index to get data after the
        previous page size, current query index, page size and the data from
        the current index to the next index. It implements a Deletion-resilient
        hypermedia pagination
        """
        assert index < len(self.__dataset)
        lst = list(self.__indexed_dataset.items())
        data = []
        i = 0
        j = index
        while i < page_size:
            if self.__indexed_dataset.get(j) is None:
                j = j + 1
                data.append(self.__indexed_dataset.get(j))
            else:
                data.append(self.__indexed_dataset.get(j))
            i = i + 1
            j = j + 1
        mydict = {
            "index": index,
            "next_index": j,
            "page_size": page_size,
            "data": data
        }
        return mydict
