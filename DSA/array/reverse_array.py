"""
Problem statement
Given an array with N elements, the task is to reverse all the array elements and print the reversed array.

Constraints:
1 <= N <= 10^3
1 <= arr[i] <= 10^9
1 <= K < N

Sample Input:
8
[7, 5, 2, 11, 2, 43, 1, 10]
Sample Output:
10 1 43 2 11 2 5 7
Explanation of Sample Input:
Here the elements have been reversed.

Test Cases:
INPUTS:
10
[11, 4, 37, 80, 3, 32, 24, 1, 23, 81]

9
[91, 40, 32, 8, 3, 32, 24, 1, 23]

15
[10, 41, 33, 85, 300, 32, 24, 10, 23, 85, 10, 11, 313, 311, 431]

OUTPUTS:
81 23 1 24 32 3 80 37 4 11

23 1 24 32 3 8 32 40 91

431 311 313 11 10 85 23 10 24 32 300 85 33 41 10

"""

manual_test = False


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    arr = []
    if manual_test:
        size = int(input("Enter input size: "))
        for i in range(0, size):
            print(f"Enter {i+1} number: ")
            arr.append(int(input()))
    else:
        # arr = [7, 5, 2, 11, 2, 43, 1, 10]
        # arr = [11, 4, 37, 80, 3, 32, 24, 1, 23, 81]
        # arr = [91, 40, 32, 8, 3, 32, 24, 1, 23]
        arr = [10, 41, 33, 85, 300, 32, 24, 10, 23, 85, 10, 11, 313, 311, 431]

    print("Array: ", arr)

    reverse_array(arr)

    print("After reverse array: ", arr)
