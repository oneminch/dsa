from data_structures.ds import *
from algorithms.algo import *

prompt = f"""
Which data structure / algorithm would you like to check out next?
\n--- DATA STRUCTURES --------\n
a) Array
b) Binary Search Tree
c) Doubly Linked List
d) Hash Table
e) Queue
f) Singly Linked List
g) Stack
h) Graph
\n--- ALGORITHMS --------\n
i) Binary Search
j) Bubble Sort
k) Selection Sort
"""

# l) Sort
# m) Sort
# n) Sort
# o) Sort
# p) Sort

fn_mappings = {
    "a": array_ds,
    "b": bst_ds,
    "c": doubly_linked_list_ds,
    "d": hash_table_ds,
    "e": queue_ds,
    "f": singly_linked_list_ds,
    "g": stack_ds,
    "h": graph_ds,
    "i": bs_algo,
    "j": bubble_sort_algo,
    "k": selection_sort_algo,
    # "l": insertion_sort_algo,
    # "m": _sort_algo,
    # "n": _sort_algo,
    # "o": _sort_algo,
    "q": None
}

choices = sorted([letter for letter in fn_mappings])

while True:
    print(prompt)
    choice = input(f"Choose a letter between 'a' and '{choices[-2]}' to continue and 'q' to quit: ")

    if choice not in fn_mappings:
        continue

    if choice == "q":
        print(f"\n{'-'*50}")
        break
    else:
        fn_mappings[choice]()

