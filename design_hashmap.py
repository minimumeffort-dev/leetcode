class MyHashMap:
    """A hash map using separate chaining with lists of key-value pairs."""

    def __init__(self) -> None:
        # Each bucket must be a separate list.
        self.buckets: list[list[tuple[int, int]]] = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[key % len(self.buckets)]
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                return
