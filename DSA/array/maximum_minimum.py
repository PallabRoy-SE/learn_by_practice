"""
Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Examples:

Input: arr[] = [3, 5, 4, 1, 9]
Output: Minimum element is: 1
        Maximum element is: 9

Input: arr[] = [22, 14, 8, 17, 35, 3]
Output: Minimum element is: 3
        Maximum element is: 35
"""

manual_test = True


def find_max_min_element(arr):
    max = arr[0]
    min = arr[0]
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num

    return max, min


if __name__ == "__main__":
    arr = []
    if manual_test:
        size = int(input("Enter input size: "))
        for i in range(0, size):
            print(f"Enter {i+1} number: ")
            arr.append(int(input()))
    else:
        # arr = [3, 5, 4, 1, 9]
        # arr = [11, 4, 37, 80, 3, 32, 24, 1, 23, 81]
        # arr = [91, 40, 32, 8, 3, 32, 24, 1, 23]
        arr = [22, 14, 8, 17, 35, 3]

    print("Array: ", arr)

    (max, min) = find_max_min_element(arr)

    print(f"Max: {max}, Min: {min}")
