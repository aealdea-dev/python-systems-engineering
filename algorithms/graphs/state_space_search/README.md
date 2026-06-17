# State Space Search: BFS Parentheses Generation

## Overview
An implementation of Breadth-First Search (BFS) to generate valid parenthetical combinations. While functionally a string generation task, this module serves as a practical implementation of **State Space Exploration**—a foundational concept in AI planning and automated configuration management.

## Technical Implementation
- **Algorithm:** Breadth-First Search (BFS) using a FIFO queue.
- **State Definition:** Each state is defined as `(current_string, open_count, close_count)`.
- **Constraint Satisfaction:** Implements strict logical boundaries (`open_count < pairs`, `close_count < open_count`) to prune invalid states from the search tree.

## Engineering Lessons Learned
- **State Space vs. String Manipulation:** Recognized that the "parentheses" problem is a proxy for exploring a decision tree. The `queue` acts as a pending state container, essential for finding the shortest path to a valid system configuration.
- **BFS vs. DFS Behavior:** Understood the necessity of BFS (`pop(0)`) to explore valid configurations level-by-level, ensuring that the system reaches the goal state through the shortest logical path.
- **Constraint Programming:** Applied conditional logic as a "guard" to prevent the system from entering invalid states—a core pattern in IIoT sensor configuration and resource management.

## Usage
```python
# Generate valid combinations for 3 pairs of parentheses
results = gen_parentheses(3)
print(results) 
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']