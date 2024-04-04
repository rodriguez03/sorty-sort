def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_recursive(arr):
    """Sorts an array using recursive bubble sort."""
    n = len(arr)
    if n == 1:
        return arr

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return [arr[0]] + bubble_sort_recursive(arr[1:])

# Examples
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

# Using standard bubble sort
sorted_arr = bubble_sort(arr.copy())
print("Sorted array using standard bubble sort:", sorted_arr)
