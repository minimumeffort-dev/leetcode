from math import isqrt


class KeyValue:
    def __init__(self, key: str, value: object) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"({self.key}, {self.value})"

    def __repr__(self) -> str:
        return f"({self.key!r}, {self.value!r})"


class HashTable:
    """A fixed-size hash table for string keys, using double hashing."""

    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise TypeError("Hash table size must be an integer")
        if size < 2 or any(
            size % divisor == 0 for divisor in range(2, isqrt(size) + 1)
        ):
            raise ValueError("Hash table size must be prime and at least 2")

        self.data: list[KeyValue | None] = [None] * size

    def check_for_key(self, key: str) -> tuple[bool, int]:
        """Return (found, index) for a matching or available slot.

        index is -1 when the key is absent and the table is full.
        """
        h1 = hash(key)
        first_index = h1 % len(self.data)
        entry = self.data[first_index]

        if entry is None:
            # key was not found
            return False, first_index
        if entry.key == key:
            # already stored in the array
            return True, first_index

        # at this point we have a collision
        h2 = hash(key + "d")
        # With a prime table size, every allowed stride reaches every slot.
        stride = h2 % (len(self.data) - 1) + 1
        second_index = (first_index + stride) % len(self.data)

        while second_index != first_index:
            entry = self.data[second_index]
            if entry is None:
                return False, second_index
            if entry.key == key:
                return True, second_index
            second_index = (second_index + stride) % len(self.data)

        # table is full
        return False, -1

    def insert(self, key: str, value: object) -> None:
        """Insert or update a value; raise OverflowError if no slot is available."""
        found, index = self.check_for_key(key)

        if index == -1:
            raise OverflowError("Hash table is full")

        if found:
            entry = self.data[index]
            assert entry is not None
            entry.value = value
        else:
            self.data[index] = KeyValue(key, value)

    def search(self, key: str) -> object:
        """Return the stored value, or raise KeyError if the key is absent."""
        found, index = self.check_for_key(key)

        if not found:
            raise KeyError(key)

        entry = self.data[index]
        assert entry is not None
        return entry.value


if __name__ == "__main__":
    ht = HashTable(7)
    print(ht.data)
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("cherry", 3)
    print(ht.data)
    print(ht.search("cherry"))
