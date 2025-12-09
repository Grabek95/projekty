# -*- coding: utf-8 -*-
"""
INTERACTIVE TEST - List append() method
Step by step understanding
"""

print("=" * 60)
print("TEST 1: Creating empty list")
print("=" * 60)

# Create empty list
shopping = []
print(f"Empty list: {shopping}")
print(f"List length: {len(shopping)}")
print()

print("=" * 60)
print("TEST 2: Adding first element with append()")
print("=" * 60)

# Add first element
shopping.append("Bread")
print(f"After adding 'Bread': {shopping}")
print(f"List length: {len(shopping)}")
print()

print("=" * 60)
print("TEST 3: Adding more elements")
print("=" * 60)

# Add more elements
shopping.append("Milk")
print(f"After adding 'Milk': {shopping}")

shopping.append("Eggs")
print(f"After adding 'Eggs': {shopping}")

shopping.append("Butter")
print(f"After adding 'Butter': {shopping}")

print(f"Final length: {len(shopping)}")
print()

print("=" * 60)
print("TEST 4: Accessing list elements (indexing)")
print("=" * 60)

# Indexing starts from 0!
print(f"First element (index 0): {shopping[0]}")
print(f"Second element (index 1): {shopping[1]}")
print(f"Last element (index -1): {shopping[-1]}")
print(f"Second to last (index -2): {shopping[-2]}")
print()

print("=" * 60)
print("TEST 5: Iterating through list")
print("=" * 60)

# Method 1: Simple loop
print("\nVersion 1 - Simple loop:")
for item in shopping:
    print(f"- {item}")

# Method 2: With numbering
print("\nVersion 2 - With numbering (enumerate):")
for i, item in enumerate(shopping):
    print(f"{i}. {item}")

# Method 3: Numbering from 1
print("\nVersion 3 - Numbering from 1:")
for i, item in enumerate(shopping, 1):
    print(f"{i}. {item}")

print()

print("=" * 60)
print("TEST 6: Checking if element is in list")
print("=" * 60)

# 'in' operator
if "Milk" in shopping:
    print("OK: Milk is on the list!")
else:
    print("X: Milk is NOT on the list")

if "Cheese" in shopping:
    print("OK: Cheese is on the list!")
else:
    print("X: Cheese is NOT on the list")

print()

print("=" * 60)
print("TEST 7: Other useful list methods")
print("=" * 60)

# count() - how many times element appears
shopping.append("Milk")  # Add duplicate
print(f"List with duplicate: {shopping}")
print(f"How many times 'Milk' appears: {shopping.count('Milk')}")

# index() - at what position is element
position = shopping.index("Eggs")
print(f"'Eggs' are at position: {position}")

# remove() - remove first matching element
shopping.remove("Milk")
print(f"After removing first 'Milk': {shopping}")

# pop() - remove and return last element
last = shopping.pop()
print(f"Removed last element: {last}")
print(f"List after pop(): {shopping}")

# insert() - insert at specific position
shopping.insert(1, "Cheese")  # Insert "Cheese" at position 1
print(f"After inserting 'Cheese' at position 1: {shopping}")

# sort() - sort alphabetically
shopping.sort()
print(f"After sorting: {shopping}")

# reverse() - reverse order
shopping.reverse()
print(f"After reversing: {shopping}")

# copy() - create a copy
backup = shopping.copy()
print(f"Created backup: {backup}")

# clear() - clear entire list
shopping.clear()
print(f"After clear(): {shopping}")
print(f"Backup (preserved): {backup}")

print()

print("=" * 60)
print("TEST 8: List comprehension (advanced)")
print("=" * 60)

# Create list in one line
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Filtering
even = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even}")

print()

print("=" * 60)
print("TEST 9: Practical example - input() + append()")
print("=" * 60)

# This is exactly what we do in the shopping list program
my_list = []

print("\nSimulating 3 additions:")
# Normally we'd use input(), but for demo we'll hardcode
items = ["Apple", "Banana", "Orange"]

for item in items:
    print(f"  User types: {item}")
    my_list.append(item)
    print(f"  After append: {my_list}")
    print()

print(f"Final list: {my_list}")

print()
print("=" * 60)
print("END OF TESTS!")
print("=" * 60)
print()
print("Now you understand:")
print("1. How to create empty list: list_name = []")
print("2. How to add elements: list_name.append(element)")
print("3. How to access elements: list_name[index]")
print("4. How to check if element exists: element in list_name")
print("5. How to iterate: for item in list_name")
print()
print("Ready for ZADANIA_TYDZIEN_1.py!")
