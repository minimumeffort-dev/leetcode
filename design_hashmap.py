"""LeetCode 706: Design HashMap, using separate chaining."""


class MyHashMap:
    """Store integer pairs in buckets; a bucket scan costs O(1 + bucket size)."""

    def __init__(self) -> None:
        # Each bucket must be a separate list.
        self.buckets: list[list[tuple[int, int]]] = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """Insert a new key or replace its existing value."""
        bucket = self.buckets[key % len(self.buckets)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                # Returning here prevents an update from adding a duplicate key.
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """Return the value, or -1 when the key is absent."""
        bucket = self.buckets[key % len(self.buckets)]
        # Different keys can share a bucket, so compare the stored keys too.
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        """Remove a key if present; removing an absent key does nothing."""
        bucket = self.buckets[key % len(self.buckets)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                return
