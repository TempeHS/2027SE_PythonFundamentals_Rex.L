class Jar:

      def __init__(self, capacity=12):
            if not isinstance(capacity, int) or capacity < 0:
                  raise ValueError("Capacity can't be negative and needs to be an int")
            self._capacity = capacity
            self._size = 0


      def __str__(self):
            return "🍪" * self._size


      def deposit(self, _):
            if self._size + _ > self._capacity:
                  raise ValueError("Not enough space")
            self._size += _


      def withdraw(self, _):
            if _ > self._size:
                  raise ValueError("Not enough cookies")
            self._size -= _


      @property
      def capacity(self):
            return self._capacity


      @property
      def size(self):
            return self._size