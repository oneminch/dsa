def binary_search(sorted_list, target):
    if len(sorted_list) == 1:
        return target == sorted_list[0]

    midpoint = len(sorted_list)//2

    if target == sorted_list[midpoint]:
        return True
    elif target > sorted_list[midpoint]:
        return binary_search(sorted_list[midpoint:], target)
    else:
        return binary_search(sorted_list[:midpoint], target)
    