class PriorityQueue(object):
    """
    A priority queue.
    """
    def __init__(self, cmp=lambda x, y: x < y):
        self.__vector = [None]
        self.cmp = cmp
        self.length = 0

    def push(self, value):
        """
        Push a value into the queue with time O(log n).
        """
        self.__vector.append(value)
        self.length += 1
        pointer = self.length
        while pointer > 1 and self.length > 1 and not self.cmp(self.__vector[pointer // 2], self.__vector[pointer]):
            temp = self.__vector[pointer // 2]
            self.__vector[pointer // 2] = self.__vector[pointer]
            self.__vector[pointer] = temp
            pointer //= 2

    def pop(self):
        """
        Pop the minimum value out of with time O(log n).
        """
        if self.length:
            self.__vector[1] = self.__vector[-1]
            self.__vector.pop(-1)
            self.length -= 1
            pointer = 1
            while (pointer <= self.length / 2 and self.length > 1 and
                   not (self.cmp(self.__vector[pointer], self.__vector[pointer * 2]) if pointer * 2 == self.length else
                        self.cmp(self.__vector[pointer], (self.__vector[pointer * 2] if
                                 self.cmp(self.__vector[pointer * 2], self.__vector[pointer * 2 + 1]) else
                                          self.__vector[pointer * 2 + 1])))):
                comparer = (0 if pointer * 2 == self.length else (0 if
                            self.cmp(self.__vector[pointer * 2], self.__vector[pointer * 2 + 1]) else 1))
                temp = self.__vector[pointer * 2 + comparer]
                self.__vector[pointer * 2 + comparer] = self.__vector[pointer]
                self.__vector[pointer] = temp
                pointer *= 2
                pointer += comparer

    @property
    def top(self):
        """
        Get the minimum value in the queue with time O(1).
        """
        if self.__vector:
            return self.__vector[1]

    @property
    def size(self):
        """
        Get the size of the queue with time O(1).
        """
        return self.length

    @property
    def empty(self):
        """
        Get the queue is empty or not with time O(1).
        """
        return self.size == 0
