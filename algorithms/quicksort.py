def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        greater = [item for item in array[1:] if item > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



print(quicksort([8,43,23,1,7,54,3,2,9,0,1]))
            