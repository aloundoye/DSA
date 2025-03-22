def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursion(arr, item, low=0, high=None):
    if high is None:
        high = len(arr) - 1  # Initialize high on the first call

    if low > high:
        return None  # Target not found

    mid = (low + high) // 2

    if arr[mid] == item:
        return mid  # Target found
    elif arr[mid] > item:
        return binary_search_recursion(arr, item, low, mid - 1)  # Search left half
    else:
        return binary_search_recursion(arr, item, mid + 1, high)  # Search right half

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search_recursion(arr, target)

if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found")


print(binary_search_recursion([1,3,5,7,9,10,12,13,23,34,45,56], 13))