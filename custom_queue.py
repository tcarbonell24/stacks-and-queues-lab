import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # TODO: Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # TODO: Remove and return the item from the front of the queue
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        # TODO: Return the item at the front of the queue without removing it
        if self.items:
            return self.items[0]
        return None

    def is_empty(self):
        # TODO: Return True if the queue is empty
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # TODO: Implement winner selection and dequeue process
        if not self.items:
            return None

        winner_index = random.randint(0, len(self.items) - 1)  # pick a random index
        winner = self.items[winner_index]

        # Remove all items up to and including winner
        self.items = self.items[winner_index + 1:]

        return winner
