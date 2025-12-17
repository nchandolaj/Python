# Part 1: The Space-Time Trade-off Deep Dive

The Space-Time Trade-off is the economic principle of computing. You have two currencies: Time (CPU cycles) and Space (Memory/RAM). You can usually "buy" speed by "spending" memory.

In an interview, the "naive" solution usually saves space but wastes time. The "optimal" solution usually spends space (via Hash Maps or Sets) to save time.

## 1. The Currencies: Big O Notation

To trade effectively, you must know the value of your currency. We use Big O to measure how costs grow as your input data (n) grows.
Time Complexity (T): If I double the input, how much longer does it take?
O(1): Instant. (e.g., Accessing an array index arr[5]).
O(\log n): Fast. Cuts problem in half each step (e.g., Binary Search).
O(n): Linear. Checks every item once (e.g., Reading a list).
O(n^2): Quadratic. Nested loops. (e.g., Comparing every item to every other item). Avoid this.
Space Complexity (S): If I double the input, how much more RAM do I need?
O(1): Constant. Uses a fixed number of variables (e.g., i, j, count).
O(n): Linear. Stores a copy of the data (e.g., A Hash Map or a new List).

## 2. The Mechanics of the Trade

The most common trade in coding interviews is Memoization (Caching).
Scenario: You need to find if an item exists in a collection.
The "Time" Heavy Approach (List Scan):
You keep data in a simple List.
To find an item, you scan the whole list.
Cost: O(n) Time, O(1) Extra Space.
The "Space" Heavy Approach (Hash Set):
You convert the List into a Hash Set. This consumes memory to organize data for instant lookup.
Cost: O(1) Time, O(n) Extra Space.

# Part 2: The First Problem - Contains Duplicate

Let's apply this concept immediately. This is the "Hello World" of Space-Time trade-offs.
Problem: [LeetCode 217] Contains Duplicate Prompt: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1, 2, 3, 1] -> Output: true
Input: nums = [1, 2, 3, 4] -> Output: false

## Solution 1: Brute Force (The "Naive" Way)

Compare every number to every other number.
def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): # Compare with every subsequent number
            if nums[i] == nums[j]:
                return True
    return False

Time: O(n^2). If nums has 10,000 items, this is 50 million operations. Too Slow.
Space: O(1). We only used i and j. Very Efficient.

## Solution 2: Sorting (The Middle Ground)

If we sort the numbers, duplicates will be next to each other (e.g., [1, 1, 2, 3]).
def containsDuplicate(nums):
    nums.sort() # Sorting takes O(n log n)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]: # Check neighbor
            return True
    return False


Time: O(n \log n). Much faster than O(n^2), but sorting is still "heavy".
Space: O(1) or O(n) depending on the sorting algorithm's internal memory usage.

## Solution 3: Hash Set (The "Space-Time Trade-off" Winner)

We trade space to get O(n) speed. We create an empty set (hash set) and check items as we go.
def containsDuplicate(nums):
    seen = set() # O(n) Space cost: We are "buying" speed with this memory
    
    for num in nums:
        if num in seen: # Lookup in a set is O(1) - Instant!
            return True
        seen.add(num)
        
    return False


Time: O(n). We walk through the list exactly once.
Space: O(n). In the worst case (no duplicates), we store every number in the set.

## Solution 4: The "Pythonic" One-Liner

In Python, we can convert the list to a set directly. A set removes duplicates automatically. If the set length is smaller than the list length, we had duplicates.
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

Time: O(n). Converting a list to a set iterates over the list once.
Space: O(n). The set requires memory.

# Summary of Trade-off for "Contains Duplicate"

Approach
Time
Space
Verdict
Brute Force
O(n^2)
O(1)
Timeout. Too slow for large inputs.
Sorting
O(n \log n)
O(1)
Acceptable. Good if memory is extremely tight.
Hash Set
O(n)
O(n)
Optimal. The industry standard solution.

Next Step: Now that you've seen the Hash Set pattern, try applying it to LeetCode 242 (Valid Anagram).
Hint: Instead of just checking if a number exists (Set), you need to count how many times it appears. You'll need a Hash Map (Dictionary) or an Array of size 26 (for a-z characters).
