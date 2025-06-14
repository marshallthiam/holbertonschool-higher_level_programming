#!/usr/bin/env python3
# task_03_countediterator.py

class CountedIterator:
    """An iterator that keeps track of the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the current count of items iterated over."""
        return self.count

    def __iter__(self):
        """Return the iterator itself."""
        return self
