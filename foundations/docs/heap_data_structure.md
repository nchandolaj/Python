# Heap

A **Heap** is a specialized, tree-based data structure that satisfies the **heap property**. While it looks like a tree, in Python, it is almost always implemented using a **List** for maximum efficiency.


## 1. The Core Concept: Min-Heap vs. Max-Heap

The "Heap Property" dictates the relationship between parent and child nodes:

* **Min-Heap:** The value of the parent node is always **less than or equal to** the values of its children. Consequently, the **root** is the smallest element.
* **Max-Heap:** The value of the parent node is always **greater than or equal to** its children. The **root** is the largest element.

### Why use a Heap instead of sorting?
If you just need the smallest element, you could sort a list (_O(N log N)_). However, if you are constantly adding new data and need the smallest element frequently, a Heap is better:
* **Get Min/Max:** $O(1)$
* **Insert/Delete:** $O(\log N)$


## 2. Python's `heapq` Module

Python provides the `heapq` module, which implements a **Min-Heap** algorithm on top of a standard list. 

> **Important Note:** Python does not have a built-in Max-Heap. To simulate one, developers typically multiply their numbers by `-1` before pushing them onto the heap.

### Essential Commands
```python
import heapq

data = [5, 1, 9, 3]

# 1. Transform a list into a heap in-place
heapq.heapify(data) # data is now [1, 3, 9, 5] (partially sorted)

# 2. Add an element
heapq.heappush(data, 2)

# 3. Remove and return the smallest element
smallest = heapq.heappop(data) # returns 1

# 4. Replace: Pop smallest and push new item in one efficient step
heapq.heapreplace(data, 10)
```

## 3. Under the Hood: The Array Representation

Even though we visualize a heap as a tree, Python stores it as a **List**. This is possible because a "Complete Binary Tree" has a predictable mathematical pattern for its indices.

For any element at index $i$:
* **Left Child:** $2i + 1$
* **Right Child:** $2i + 2$
* **Parent:** $(i - 1) // 2$

This array-based storage is incredibly memory-efficient because it avoids the overhead of creating "Node" objects with pointers (like you would in a Linked List).


## 4. Real-World Use Cases

### A. Priority Queues
In a standard Queue, the first person in line is served first. In a **Priority Queue**, the person with the "highest priority" (lowest numerical value in a Min-Heap) is served first, regardless of when they arrived.
* *Example:* OS task scheduling or hospital triage.

### B. The "Top K" Problem
As seen in the "Top K" question, if you have 1 million elements and want the 10 most frequent, you don't need to sort all 1 million. You maintain a heap of size 10, resulting in much faster performance.

### C. Merging Sorted Streams
If you have multiple sorted log files and want to merge them into one master sorted file, `heapq.merge()` is the most memory-efficient way to do it.


## 5. Complexity Summary

| Operation | Complexity | Description |
| :--- | :--- | :--- |
| **Heapify** | $O(N)$ | Turning a random list into a heap. |
| **Push** | $O(\log N)$ | Adding an element and "bubbling" it up. |
| **Pop** | $O(\log N)$ | Removing the root and "sifting" down. |
| **Peek** | $O(1)$ | Accessing `heap[0]` to see the smallest item. |

---
# Max-Heap Implementation

In Python, since the `heapq` module only provides a Min-Heap, we have to be a bit clever to achieve **Max-Heap** behavior. The most common "trick" is to invert the sign of the numbers.

## The Max-Heap "Negative Number" Trick

Because a Min-Heap always keeps the *smallest* value at the root, if we multiply all our values by `-1`, the "mathematically smallest" value becomes the one that was originally the largest.

**Example:** If we have `[1, 10, 5]`, and we want a Max-Heap:
1.  Convert them to `[-1, -10, -5]`.
2.  The Min-Heap will put `-10` at the root (since $-10 < -1$).
3.  When we pop `-10`, we multiply by `-1` again to get our original `10` back.

### Implementation Example

```python
import heapq

# Original data
scores = [10, 50, 20, 400, 30]

# 1. Push elements as negative values
max_heap = []
for s in scores:
    heapq.heappush(max_heap, -s)

# 2. To see the 'max' value (the root)
# We access index 0 and flip it back
print(f"Max value: {-max_heap[0]}") # Output: 400

# 3. To pop the largest value
largest = -heapq.heappop(max_heap)
print(f"Popped: {largest}") # Output: 400

# 4. The new root
print(f"New Max: {-max_heap[0]}") # Output: 50
```

## Max-Heap with Tuples (Priority Objects)

Often, you aren't just storing numbers; you're storing objects (like Tasks) with a priority. Python's `heapq` handles tuples by comparing the first element first.

```python
import heapq

# Format: (Priority, TaskName)
# Since it's a Min-Heap, lower numbers usually come first.
# To make it a Max-Priority Queue, we negate the priority.

tasks = []
heapq.heappush(tasks, (-10, "Critical Update"))
heapq.heappush(tasks, (-1, "Fix typo"))
heapq.heappush(tasks, (-5, "Feature request"))

# Pop the highest priority task
priority, task = heapq.heappop(tasks)
print(f"Executing: {task} (Priority Level: {-priority})")
# Output: Executing: Critical Update (Priority Level: 10)
```

## Why this matters for the "Top K" problem

When solving "Top K Frequent Elements," you have two choices depending on which heap you use:

1.  **Min-Heap of size K:** (As shown in the first response) You keep the "best" $k$ elements and discard the smallest ones as you go. This is $O(N \log K)$.
2.  **Max-Heap of all elements:** You put everything into a Max-Heap ($O(N)$) and then pop $k$ times ($O(K \log N)$).

### Summary Table: Min vs Max in Python

| Feature | Min-Heap (Default) | Max-Heap (Workaround) |
| :--- | :--- | :--- |
| **Logic** | `parent <= children` | `parent >= children` |
| **Root** | `heap[0]` (Smallest) | `-heap[0]` (Largest) |
| **Insertion** | `heappush(h, val)` | `heappush(h, -val)` |
| **Extraction** | `heappop(h)` | `-heappop(h)` |
