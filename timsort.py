def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # Loop from the element indicated by
    # `left` until the element indicated by `right`
    for i in range(left + 1, right + 1):
        # This is the element we want to position in its
        # correct place
        key_item = arr[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= left and arr[j] > key_item:
            # Shift the value one position to the right
            # and reposition j to point to the next element
            # (from right to left)
            arr[j + 1] = arr[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        arr[j + 1] = key_item

    return arr

def timsort(arr):
    min_run = 32
    n = len(arr)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the mid-point
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `mid + 1`, while the `right` array should
            # go from `mid + 1` to `end + 1`.
            left = arr[start:mid + 1]
            right = arr[mid + 1:end + 1]

            # Compute the total length of
            # the `merged` array
            merged = [None] * (len(left) + len(right))

            # Initialize pointers to the start of each array
            left_pointer = 0
            right_pointer = 0
            merged_pointer = 0

            # Merge the two arrays together
            while left_pointer < len(left) and right_pointer < len(right):
                # If the left value is smaller (or equal)
                # than the right value, take the left value
                if left[left_pointer] <= right[right_pointer]:
                    merged[merged_pointer] = left[left_pointer]
                    left_pointer += 1
                else:
                    merged[merged_pointer] = right[right_pointer]
                    right_pointer += 1

                # Move to the next slot
                merged_pointer += 1

            # Copy the remaining elements into `merged`
            while left_pointer < len(left):
                merged[merged_pointer] = left[left_pointer]
                left_pointer += 1
                merged_pointer += 1

            while right_pointer < len(right):
                merged[merged_pointer] = right[right_pointer]
                right_pointer += 1
                merged_pointer += 1

            # Copy the `merged` array back into `arr`
            arr[start:start + len(merged)] = merged

        # Each iteration should double the size of your arrays
        size *= 2

    return arr