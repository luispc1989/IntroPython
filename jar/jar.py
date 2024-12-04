class Jar:
    def __init__(self, capacity=12):
        """
        Initializes the cookie jar with a specific capacity.
        Raises ValueError if capacity is not a non-negative integer.
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0  # The jar starts empty.

    def __str__(self):
        """
        Returns a string representation of the cookies in the jar.
        """
        return "🍪" * self._size

    def deposit(self, n):
        """
        Adds `n` cookies to the jar.
        Raises ValueError if `n` is negative or if it exceeds the jar's capacity.
        """
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._size + n > self._capacity:
            raise ValueError("The number of cookies exceeds the jar's capacity.")
        self._size += n

    def withdraw(self, n):
        """
        Removes `n` cookies from the jar.
        Raises ValueError if `n` is negative or if there are fewer cookies than required.
        """
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self._size:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        """
        Returns the maximum capacity of the jar.
        """
        return self._capacity

    @property
    def size(self):
        """
        Returns the current number of cookies in the jar.
        """
        return self._size


def main():
    jar = Jar()
    print(jar)  # Should print an empty string
    jar.deposit(1)
    print(jar)  # Should print "🍪"
    jar.deposit(3)
    print(jar)  # Should print "🍪🍪🍪🍪"
    jar.withdraw(2)
    print(jar)  # Should print "🍪🍪"


if __name__ == "__main__":
    main()
