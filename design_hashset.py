class MyHashSet:
    """A hash set for integer keys, using separate chaining."""

    def __init__(self) -> None:
        self.buckets: list[list[int]] = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        if key not in bucket:
            bucket.append(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key % len(self.buckets)]
        return key in bucket

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        for index, stored_key in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                return
