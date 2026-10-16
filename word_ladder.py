"""LeetCode 127: Word Ladder, using BFS with wildcard pattern buckets.

Problem: https://leetcode.com/problems/word-ladder/
"""

from collections import defaultdict, deque


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> int:
        """Return the shortest sequence's word count, or 0 if none exists.

        Let N be the number of distinct words including beginWord, and L
        their length. Expected time is O(N * L²): each word generates L
        patterns, each taking O(L) to build and hash, during setup and BFS.
        Each bucket is scanned once, so at most N * L neighbour entries
        are examined. Hash table access takes O(1) expected time after hashing.

        Extra space is O(N * L²) in the worst case: there can be N * L
        distinct pattern keys of length L. The buckets also store N * L
        word references; the word set, visited set and queue use O(N) space.
        The caller's wordList is left unchanged.
        """
        words = set(wordList)
        if endWord not in words:
            return 0
        words.add(beginWord)

        buckets: defaultdict[str, list[str]] = defaultdict(list)
        for word in words:
            for index in range(len(word)):
                # Words such as "hot" and "hit" share the pattern "h*t".
                pattern = word[:index] + "*" + word[index + 1:]
                buckets[pattern].append(word)

        queue = deque([beginWord])
        visited = {beginWord}
        path_length = 1  # Count words, including beginWord, rather than changes.

        while queue:
            # Newly queued words belong to the next sequence length.
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return path_length

                for index in range(len(word)):
                    pattern = word[:index] + "*" + word[index + 1:]
                    # This scan discovers every word in the bucket. Removing it
                    # avoids repeating that work when another word uses it.
                    for neighbour in buckets.pop(pattern, []):
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)

            path_length += 1

        return 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            "LeetCode example",
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5,
        ),
        (
            "End word missing",
            "hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0,
        ),
        ("End word present but disconnected", "hit", "cog", ["hot", "cog"], 0),
        ("Direct transformation", "hit", "hot", ["hot"], 2),
        ("Begin word already present", "hit", "hot", ["hit", "hot"], 2),
        ("Single-letter words", "a", "c", ["a", "b", "c"], 2),
        (
            "Several shortest sequences",
            "red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex"], 4,
        ),
        ("Cycles between words", "aaa", "bbb", ["aab", "aba", "abb", "bbb"], 4),
        ("Missing intermediate words", "hit", "cog", ["cog"], 0),
        (
            "Ten-letter chain",
            "aaaaaaaaaa",
            "bbbbbbbbbb",
            ["b" * count + "a" * (10 - count) for count in range(1, 11)],
            11,
        ),
    ]

    for name, begin_word, end_word, word_list, expected in test_cases:
        original = word_list.copy()
        found = solution.ladderLength(begin_word, end_word, word_list)
        print(f"{name}: length={found}, expected={expected}")
        assert found == expected, name
        assert word_list == original, f"{name}: input list was changed"
