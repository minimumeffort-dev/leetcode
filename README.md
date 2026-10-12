# LeetCode

I'm working through LeetCode in Python and implementing the data structures behind the problems. I keep different versions when they help compare the approaches.

The comments explain the main ideas, and the docstrings note input assumptions and time or space costs.

## Problems

| File | What it does |
| --- | --- |
| [two_sum.py](two_sum.py) | Finds two numbers that add up to the target using a dictionary of values already seen. |
| [merge_strings_alternately.py](merge_strings_alternately.py) | Alternates characters from two strings, then adds the remaining tail. |
| [greatest_common_divisor_of_strings.py](greatest_common_divisor_of_strings.py) | Checks that both strings share a repeating pattern, then finds its largest possible length with GCD. |
| [kids_with_the_greatest_number_of_candies.py](kids_with_the_greatest_number_of_candies.py) | Checks which kids could reach the current maximum after receiving the extra candies. |
| [can_place_flowers.py](can_place_flowers.py) | Finds valid planting spots by checking neighboring plots and skipping ahead after a placement. |
| [reverse_vowels_of_a_string.py](reverse_vowels_of_a_string.py) | Uses two pointers to swap vowels from opposite ends of the string. |
| [hash_map_separate_chaining.py](hash_map_separate_chaining.py) | Builds a hash map with buckets of key-value pairs and separate chaining. |
| [hash_set_separate_chaining.py](hash_set_separate_chaining.py) | Builds a hash set with buckets, handling collisions by keeping keys in the same bucket. |
| [group_anagrams_sorting.py](group_anagrams_sorting.py) | Groups anagrams by sorting the letters in each word. |
| [group_anagrams_letter_counts.py](group_anagrams_letter_counts.py) | Groups lowercase English anagrams using their 26 letter counts. |
| [longest_consecutive_sequence.py](longest_consecutive_sequence.py) | Uses a set and only counts consecutive runs from their first number. |
| [merge_two_sorted_lists.py](merge_two_sorted_lists.py) | Merges two sorted linked lists by reconnecting their existing nodes. |
| [remove_duplicates_from_sorted_list.py](remove_duplicates_from_sorted_list.py) | Removes repeated values from a sorted linked list by skipping duplicate nodes. |
| [remove_linked_list_elements.py](remove_linked_list_elements.py) | Removes matching nodes, including any at the beginning of the list. |
| [reverse_linked_list.py](reverse_linked_list.py) | Reverses a linked list iteratively, with a recursive version alongside it. |
| [move_zeroes.py](move_zeroes.py) | Moves zeros to the end while keeping the other values in their original order. |
| [longest_palindromic_substring_brute_force.py](longest_palindromic_substring_brute_force.py) | Checks candidate substrings directly, skipping lengths that cannot improve the answer. |
| [longest_palindromic_substring_center_expansion.py](longest_palindromic_substring_center_expansion.py) | Expands around character and gap centers to find the longest palindrome in O(n²) time. |
| [longest_palindromic_substring_manacher.py](longest_palindromic_substring_manacher.py) | Uses Manacher's algorithm to reuse palindrome symmetry and finish in O(n) time. |
| [merge_intervals.py](merge_intervals.py) | Sorts intervals by their start, then combines overlapping ranges in one pass. |
| [meeting_rooms_ii.py](meeting_rooms_ii.py) | Sorts meetings by their start and reuses rooms with a min-heap of end times. |

## Algorithms and data structures

| File | What it does |
| --- | --- |
| [binary_search.py](binary_search.py) | Finds a value in a sorted list by repeatedly halving the search range. |
| [bubble_sort.py](bubble_sort.py) | Swaps neighboring values until a full pass makes no changes. |
| [insertion_sort.py](insertion_sort.py) | Grows a sorted prefix by shifting larger values and inserting the next number. |
| [merge_sort.py](merge_sort.py) | Recursively sorts two halves, then merges them back into the original list. |
| [quick_sort.py](quick_sort.py) | Sorts in place with a random pivot and two-way partitioning. |
| [hash_table_double_hashing.py](hash_table_double_hashing.py) | Uses a second hash to handle collisions in a fixed-size table. |
| [max_heap.py](max_heap.py) | Implements a max heap with insertion, removal of the maximum, and sifting in both directions. |
| [build_max_heap.py](build_max_heap.py) | Builds a max heap from an existing list by sifting parents down from the bottom. |
| [doubly_linked_list.py](doubly_linked_list.py) | Implements a doubly linked list with head insertion, search, deletion, and a readable display. |
| [binary_tree_traversals.py](binary_tree_traversals.py) | Defines a binary-tree node with recursive `preorder()`, `inorder()`, and `postorder()` methods and a sideways tree display. |
| [binary_tree_sum.py](binary_tree_sum.py) | Builds a binary tree, prints it sideways, and recursively sums its values. |
| [factorial_and_fibonacci.py](factorial_and_fibonacci.py) | Practices direct recursion with factorial and Fibonacci, including zero base cases and checks for negative inputs. |
| [running_median_insertion_sort_compact.py](running_median_insertion_sort_compact.py) | Prints a running median by inserting each new number into a sorted list. |
| [running_median_insertion_sort.py](running_median_insertion_sort.py) | Another version of the same running-median approach, with the insertion steps broken out. |

## Running the examples

Use Python 3.10 or later. There are no third-party dependencies.

Files with a `__main__` block can be run directly:

```bash
python3 max_heap.py
python3 binary_tree_sum.py
python3 merge_sort.py
```

The problem solutions keep the class and method names expected by LeetCode. Linked-list solutions also include a node class so they can be used locally.

[AGENTS.md](AGENTS.md) records how solutions should be reviewed, documented, and published. [.gitignore](.gitignore) keeps local caches and environment files out of the repo.
