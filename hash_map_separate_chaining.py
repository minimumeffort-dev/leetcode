"""LeetCode 706: Design HashMap, using separate chaining."""


class MyHashMap:
    """Store integer pairs in buckets using separate chaining.

    Choosing a bucket is O(1). If it holds k entries, scanning it costs
    O(1 + k), with O(n) worst-case time when all n keys share a bucket.
    Uniformly spread keys give expected k = n / B for B buckets; B is fixed
    at 1000 here. The B lists and n stored pairs use O(B + n) space.
    """

    def __init__(self) -> None:
        """Creating B separate bucket lists costs O(B) time and space."""
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
                # pop also shifts later bucket entries, adding at most O(k) work.
                bucket.pop(index)
                return
