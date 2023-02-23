from data_structures.ds import *
from algorithms.algo import *

prompt = f"""
Which data structure / algorithm would you like to check out next?
\n--- DATA STRUCTURES --------\n
1) Array
2) Hash Table
3) Singly Linked List
4) Doubly Linked List
5) Stack
6) Queue
\n--- ALGORITHMS --------\n
8) Binary Search
"""

while True:
    print(prompt)
    choice = int(input("Choose from 1 - 5 to continue and '0' to quit: "))

    if choice not in range(0, 7):
        continue

    if choice == 0:
        print(f"\n{'-'*50}")
        break
    elif choice == 1:
        array_ds()
    elif choice == 2:
        hash_table_ds()
    elif choice == 3:
        linked_list_ds()
    elif choice == 4:
        doubly_linked_list_ds()
    elif choice == 5:
        stack_ds()
    elif choice == 6:
        queue_ds()
    elif choice == 8:
        bs_algo()
