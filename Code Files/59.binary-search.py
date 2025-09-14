    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    sorted_list = [10, 20, 30, 40, 50]
    result = binary_search(sorted_list, 40)
    print(f"Binary Search: Element found at index {result}") # Output: 3