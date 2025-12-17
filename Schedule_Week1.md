# Week 1: A comprehensive, day-by-day plan
**Theme**: Python Mastery & Algorithmic Patterns. </br>
**Goal**: By Sunday, you must be able to solve "Easy" and "Medium" array/string problems optimally (in O(n) time) and write Python code that looks like it was written by a senior engineer.

## Learning Objectives
1. **Pattern Recognition**: Master Two Pointers and Sliding Window techniques.
2. **Language Fluency**: Stop writing "Java-style" Python. Use list comprehensions, enumerate, zip, and defaultdict.
3. **Complexity Analysis**: Be able to state the Time and Space complexity for every single line of code you write.

## Daily Schedule

### Monday: The Pythonic Standard
_Focus: Writing clean, idiomatic code and understanding complexity._
- **Concept Review** (1 Hour):
  - **Big O Notation**: Review Time vs. Space complexity. Understand why O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2).
  - **Python Internals**:
    - List vs. Tuple vs. Set (Lookup times).
    - dict implementation (Hash map).
    - List slicing arr[start:stop:step] (Note: Slicing creates a copy, costing O(k) memory).
- **Coding Practice** (2 Problems):
  1. Contains Duplicate (LeetCode 217) - Goal: Solve using a Set (O(n)).
  2. Valid Anagram (LeetCode 242) - Goal: Solve using a Hash Map or Array counting.
- Reading: "Effective Python" - Item 6 (Prefer Multiple Assignment Unpacking) & Item 11 (Slice Sequences).

### Tuesday: Arrays & Hashing
_Focus: Using Hash Maps to trade space for time._
- **Concept Review** (30 mins):
  - **Hashing**: Collisions, Load Factor.
  - **The "Pre-computation" Pattern**: Storing seen elements in a map to check for existence in O(1).
- **Coding Practice** (2 Problems):
  1. **Two Sum** (LeetCode 1) - The classic. Do not use a double for-loop.
  2. **Group Anagrams** (LeetCode 49) - Focus: How to key a hash map with a list (you can't; use a tuple).

### Wednesday: Two Pointers (Part I)
_Focus: Reducing O(n^2) to O(n) by processing from both ends._
- **Concept Review** (30 mins):
  - **Pattern**: One pointer at the start (L), one at the end (R). Move them based on a condition.
  - **Use Case**: Sorted arrays, Palindromes.
- **Coding Practice** (2 Problems):
  1. **Valid Palindrome** (LeetCode 125) - Handle non-alphanumeric chars efficiently.
  2. **Two Sum II - Input Array Is Sorted** (LeetCode 167) - Must use constant extra space.

### Thursday: Two Pointers (Part II)
_Focus: Advanced Two Pointers (The "3Sum" hurdle)._
- **Concept Review** (30 mins):
  - Handling duplicates in Two Pointer solutions.
  - Lambda Functions: Learn to sort complex lists, e.g., data.sort(key=lambda x: x[1]).
- **Coding Practice** (2 Problems):
  1. **3Sum** (LeetCode 15) - This is a "Gatekeeper" problem. If you can't solve this comfortably, you aren't ready for Facebook/Google.
  2. **Container With Most Water** (LeetCode 11) - Focus on the greedy logic of moving the shorter wall.

### Friday: Sliding Window (Fixed & Variable)
_Focus: Processing subarrays efficiently._
- **Concept Review** (30 mins):
  - **Pattern**: Expand Right pointer to include data, shrink Left pointer to satisfy constraints.
  - **MLE Relevance**: This mimics processing time-series data streams.
- **Coding Practice** (2 Problems):
  1. **Best Time to Buy and Sell Stock** (LeetCode 121).
  2. **Longest Substring Without Repeating Characters** (LeetCode 3).

### Saturday: The "Mini-Mock" (Timed)
_Focus: Simulating interview pressure._
- **Setup**: 60 Minutes, No Google, No Autocomplete (Use a plain text editor or whiteboard).
- **Task**: Solve these 3 problems back-to-back:
  1. **Product of Array Except Self** (LeetCode 238) - Constraint: No Division allowed. O(n).
  2. **Top K Frequent Elements** (LeetCode 347) - Try using a Heap or Bucket Sort.
  3. **Encode and Decode Strings** (LeetCode 271 or similar).

### Sunday: Review & MLE Context
_Focus: Connecting code to Machine Learning._
- **Review**: Look at the "Discussion" tab on LeetCode for the problems you struggled with.
- **MLE Context**:
  - Review numpy basics. How would you do "Two Sum" logic using numpy masking? (Mental exercise).
  - _Self-Correction_: If you struggled with **Recursion** or **Classes**, read up on them tonight to prep for Week 2 (Linked Lists/Trees).

### Week 1 Checkpoints
| **Topic** | **Passing Criteria** |
| ----- | ---------------- | 
| **Space Complexity** | Can you explain the difference between creating a new list res = [] vs modifying in-place? |
| **Hash Maps** | Can you implement a Counter without importing collections.Counter? |
| **Loops** | Are you comfortable traversing an array backwards? range(len(nums)-1, -1, -1) |
| **Edge Cases** | Did you remember to check for Empty Arrays? Arrays with 1 element? |

## Recommended Resources for Week 1
1. **NeetCode.io**: "Arrays & Hashing" and "Two Pointers" roadmaps.
2. **Python Library Reference**: Read the documentation for collections.deque and heapq.
3. **Visualizer**: PythonTutor.com (If you get stuck on how pointers move).
