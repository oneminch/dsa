from algorithms.binary_search import binary_search
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
# from algorithms._sort import _sort
# from algorithms._sort import _sort
# from algorithms._sort import _sort
# from algorithms._sort import _sort
# from algorithms._sort import _sort


def bs_algo():
    lst_1 = [1, 2, 3, 5, 6, 7, 9, 11, 34, 56, 67]
    target_1 = 1
    print(f"\nIs {target_1} in {lst_1}? ", binary_search(lst_1, target_1))

    lst_2 = ["ab", "cd", "ef", "gh", "ij", "kl"]
    target_2 = "ij"
    print(f"\nIs {target_2} in {lst_2}? ", binary_search(lst_2, target_2))


def bubble_sort_algo():
    lst = [99, 2, 35, 5, 46, 7, 19, 11, 34, 5, 67]

    print(f"\nList to sort: {lst}")
    
    bubble_sort(lst)
    
    print(f"\nSorted list: {lst}")
    

def selection_sort_algo():
    lst = [99, 2, 35, 5, 46, 7, 19, 11, 34, 5, 67]

    print(f"\nList to sort: {lst}")
    
    selection_sort(lst)
    
    print(f"\nSorted list: {lst}")
    
    
# def insertion_sort_algo():
#     lst = [99, 2, 35, 5, 46, 7, 19, 11, 34, 5, 67]

#     print(f"\nList to sort: {lst}")
    
#     insertion_sort(lst)
    
#     print(f"\nSorted list: {lst}")


# def _sort_algo():
#     lst = [99, 2, 35, 5, 46, 7, 19, 11, 34, 5, 67]

#     print(f"\nList to sort: {lst}")
    
#     _sort(lst)
    
#     print(f"\nSorted list: {lst}")