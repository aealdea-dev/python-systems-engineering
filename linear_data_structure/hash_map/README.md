# Hash Table: Implementation & Hashing Strategy

## Purpose
A from-scratch implementation of a `HashTable` to explore the mechanics of key-value storage, hash functions, and collision resolution. This module serves as an investigation into how high-level data structures (like Python's `dict`) manage memory and search performance at an algorithmic level.

## Key Learning Outcomes
- **Hashing Logic:** Implemented a summation-based hashing function using `ord()` to map variable-length strings to discrete integer keys.
- **Collision Resolution:** Utilized nested dictionary structures to handle "collisions"—instances where different keys generate the same hash value—ensuring data integrity without overwriting existing entries.
- **Algorithmic Complexity:** Explored the trade-offs of $O(1)$ lookup performance versus the memory overhead of managing nested buckets.
- **Architectural Isolation:** Refactored state management to utilize `__init__` instance variables, ensuring complete data isolation between separate `HashTable` objects.

## Learning Note
*This implementation was developed as part of a structured systems engineering curriculum. Initial challenges regarding class-level vs. instance-level state management and collision handling were resolved through iterative peer-guided debugging. This process clarified the distinction between high-level language abstractions and the underlying data structure mechanics.*