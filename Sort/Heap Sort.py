def heap_sort(arr):
    """
    Heap Sort: Builds a max-heap and repeatedly extracts the maximum element.
    """
    def heapify(arr, n, i):
        """Ensure subtree rooted at i is a max-heap."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build max-heap (start from last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current max to end
        heapify(arr, i, 0)              # Heapify reduced heap

    return arr
