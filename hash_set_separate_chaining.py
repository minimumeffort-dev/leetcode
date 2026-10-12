"""LeetCode 705: Design HashSet, using separate chaining."""


class MyHashSet:
    """Store integer keys in buckets; a bucket scan costs O(1 + bucket size)."""

    def __init__(self) -> None:
        # Separate lists prevent an insertion from appearing in every bucket.
        self.buckets: list[list[int]] = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        """Add a key once, even if add is called repeatedly."""
        bucket = self.buckets[key % len(self.buckets)]
        if key not in bucket:
            bucket.append(key)

    def contains(self, key: int) -> bool:
        """Check the key itself because several keys may share a bucket."""
        bucket = self.buckets[key % len(self.buckets)]
        return key in bucket

    def remove(self, key: int) -> None:
        """Remove a key if present; removing an absent key does nothing."""
        bucket = self.buckets[key % len(self.buckets)]
        for index, stored_key in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                return
