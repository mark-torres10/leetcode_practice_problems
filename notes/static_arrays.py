def insert_value(arr, val, idx):
    """Inserts a new value at a specific index in an array (as opposed to
    replacing the value at that index)."""
    pass


def delete_value(arr, idx):
    """Deletes a value at a specific index in an array.
    
    Takes the values after the index and shifts them to the left by one.

    Time complexity: O(n)
    Space complexity: O(1) (in place)
    """
    for i in range(idx + 1, len(arr)):
        arr[i - 1] = arr[i]
    arr.pop()
    return arr
