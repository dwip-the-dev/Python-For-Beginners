    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i  # Return the index if found
        return -1 # Return -1 if not found

    my_list = [10, 20, 30, 40, 50]
    result = linear_search(my_list, 30)
    print(f"Linear Search: Element found at index {result}") # Output: 2