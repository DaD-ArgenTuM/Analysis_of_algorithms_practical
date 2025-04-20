def merge_sort(arr):
    # Base case: a list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Conquer (Merge the sorted halves)
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements (if any)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

