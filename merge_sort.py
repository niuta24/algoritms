def merge_sort(lst:list)->list:
    """Creates a merge sort alghoritm

    Args:
        lst (list): list of values

    Returns:
        list: sorted list
    >>> merge_sort([4, 2, 10, 1, 16, 6, 45, 45, 65])
    [1, 2, 4, 6, 10, 16, 45, 45, 65]
    >>> merge_sort([3, 10, 4, 11, 16, 36, 45, 65])
    [3, 4, 10, 11, 16, 36, 45, 65]
    """
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k]=right[j]
            j += 1
            k += 1
    return lst