from data_structures.ds import *
from algorithms.algo import *

prompt = f"""
Which data structure / algorithm would you like to check out next?
\n--- DATA STRUCTURES --------\n
1) Array
2) Hash Table
3) Singly Linked List
4) Doubly Linked List
\n--- ALGORITHMS --------\n
5) Binary Search
"""

while True:
    print(prompt)
    choice = int(input("Choose from 1 - 5 to continue and '0' to quit: "))

    if choice not in range(0, 6):
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
        bs_algo()
