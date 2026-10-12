"""LeetCode 705: Design HashSet, using separate chaining."""


class MyHashSet:
    """Store integer keys in buckets using separate chaining.

    Choosing a bucket is O(1), then membership scans its k keys in O(1 + k).
    Worst-case time is O(n) when all n keys share a bucket. Uniform keys
    give expected k = n / B for B buckets; B stays at 1000 in this version.
    The B lists and n stored keys use O(B + n) space.
    """

    def __init__(self) -> None:
        """Creating B separate bucket lists costs O(B) time and space."""
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
                # pop shifts the later keys, still within the O(k) bucket bound.
                bucket.pop(index)
                return
