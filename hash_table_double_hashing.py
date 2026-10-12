"""A fixed-size string-key hash table with double hashing."""

from math import isqrt


class KeyValue:
    """One stored entry, with readable representations for printing the table."""

    def __init__(self, key: str, value: object) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"({self.key}, {self.value})"

    def __repr__(self) -> str:
        # !r preserves string quotes when entries appear inside a printed list.
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
        first_index = hash(key) % len(self.data)
        entry = self.data[first_index]

        if entry is None:
            return False, first_index
        if entry.key == key:
            return True, first_index

        # A prime capacity and a nonzero stride visit every slot before wrapping.
        stride = hash(key + "d") % (len(self.data) - 1) + 1
        second_index = (first_index + stride) % len(self.data)

        while second_index != first_index:
            entry = self.data[second_index]
            if entry is None:
                return False, second_index
            if entry.key == key:
                return True, second_index
            second_index = (second_index + stride) % len(self.data)

        # Returning to the first slot means every possible position was checked.
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
    table = HashTable(7)
    print(table.data)
    table.insert("apple", 1)
    table.insert("banana", 2)
    table.insert("cherry", 3)
    print(table.data)
    print(table.search("cherry"))
