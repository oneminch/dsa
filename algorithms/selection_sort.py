def selection_sort(array):
    for i, m in enumerate(array[:-1]):
        smallestIndex = i    
        for j, n in enumerate(array[i+1:]):
            if n < array[smallestIndex]:
                smallestIndex = j+i+1

        if smallestIndex != i:
            array[i], array[smallestIndex] = array[smallestIndex], array[i]
            