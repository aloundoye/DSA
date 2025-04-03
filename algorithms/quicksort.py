def quicksort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2  # Find the middle index
        pivot = array[mid]  # Use the middle element as the pivot
        
        # Create the less and greater sublists (excluding the pivot)
        less = [item for i, item in enumerate(array) if item <= pivot and i != mid]
        greater = [item for i, item in enumerate(array) if item > pivot and i != mid]

        return quicksort(less) + [pivot] + quicksort(greater)



# print(quicksort([8,43,23,1,7,54,3,2,9,0,1,8,43,23,1,7,54,3,2,9,0,1,]))
print(quicksort([0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 7, 7, 8, 8, 9, 9, 23, 23, 43, 43, 54, 54]))
            