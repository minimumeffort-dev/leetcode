"""A fixed-size string-key hash table with double hashing."""

from math import isqrt


class KeyValue:
    """One fixed-size entry holding key/value references, using O(1) storage.

    Formatting an entry creates text whose cost depends on its displayed size
    and the value object's conversion methods.
    """

    def __init__(self, key: str, value: object) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"({self.key}, {self.value})"

    def __repr__(self) -> str:
        # !r preserves string quotes when entries appear inside a printed list.
        return f"({self.key!r}, {self.value!r})"


class HashTable:
    """A fixed-size hash table for string keys, using double hashing.

    An array of m slots uses O(m) reference storage, excluding key/value objects.
    Lookup costs also depend on the key length; see check_for_key below.
    """

    def __init__(self, size: int) -> None:
        """Allocate m slots in O(m) time/space after O(sqrt(m)) prime checking.

        Testing divisors only through sqrt(m) is enough: a composite number
        has at least one factor at or below its square root. Creating the
        m-element slot list dominates the valid-table initialization cost.
        """
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

        At most m slots are probed. For a key of length k, string hashing
        and comparisons can cost O(k + 1), giving O(m * (k + 1)) worst-case
        time. With low load and well-distributed hashes, expected probes
        are constant, giving expected O(k + 1) time. The second hash creates
        key + "d", using O(k + 1) temporary space; probe indices use O(1).
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
        """Insert or update a value; raise OverflowError if no slot is available.

        Probing has the cost described in check_for_key. Updating a value
        or creating one fixed-size entry adds O(1) work and storage.
        """
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
        """Return the stored value, or raise KeyError if the key is absent.

        Probing has the cost described in check_for_key. Returning the value
        itself is O(1), because its object is referenced rather than copied.
        """
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
