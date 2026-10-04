"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # I chose a set because sets only store unique values and provide fast
    # membership checking. Each lookup and insertion is expected to take O(1)
    # average time, so checking the entire list takes O(n) time.
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


# Test cases
print(has_duplicates([10, 20, 30, 20, 40]))  # True
print(has_duplicates([1, 2, 3, 4, 5]))        # False
print(has_duplicates([]))                     # False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support
removing tasks from the front.

Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() -> "Email follow-up"
"""

from collections import deque


class TaskQueue:
    def __init__(self):
        # I chose a queue because tasks need to be handled in FIFO
        # (first in, first out) order. A deque allows adding to the end and
        # removing from the front in O(1) time.
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None

        return self.tasks.popleft()


# Test cases
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")

print(task_queue.remove_oldest_task())  # Email follow-up
print(task_queue.remove_oldest_task())  # Code review
print(task_queue.remove_oldest_task())  # None


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to
return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() -> 2
"""


class UniqueTracker:
    def __init__(self):
        # I chose a set because it automatically keeps only unique values.
        # Adding a value takes O(1) average time, and getting the number of
        # stored unique values using len() also takes O(1) time.
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Test cases
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)

print(tracker.get_unique_count())  # 2

tracker.add(30)
print(tracker.get_unique_count())  # 3