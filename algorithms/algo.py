from algorithms.binary_search import binary_search


def bs_algo():
    lst_1 = [1, 2, 3, 5, 6, 7, 9, 11, 34, 56, 67]
    target_1 = 1
    print(f"Is {target_1} in {lst_1}? ", binary_search(lst_1, target_1))

    lst_2 = ["ab", "cd", "ef", "gh", "ij", "kl"]
    target_2 = "ij"
    print(f"Is {target_2} in {lst_2}? ", binary_search(lst_2, target_2))
