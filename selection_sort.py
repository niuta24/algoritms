def selection_sort(lst:list)->list:
    """Doing selection sprt alghoritm

    Args:
        lst (list): list of values

    Returns:
        list: sorted list
    >>> selection_sort([4, 2, 10, 1, 16, 6, 45, 45, 65])
    [1, 2, 4, 6, 10, 16, 45, 45, 65]
    >>> selection_sort([3, 4, 10, 11, 16, 36, 45, 65])
    [3, 4, 10, 11, 16, 36, 45, 65]
    """
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j]<lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
