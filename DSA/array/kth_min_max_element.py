"""
Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest and largest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7 and 10
Explanation: 3rd smallest and largest elements in the given array are 7 and 10.
Input: arr[] = [2, 3, 1, 20, 15], k = 4
Output: 15 and 2
Explanation: 4th smallest and largest elements in the given array are 15 and 2.
Constraints:
1 <= arr.size <= 106
1<= arr[i] <= 106
1 <= k <= n

Expected Complexities
Time Complexity: O(n + max_element)
Auxiliary Space: O(n + max_element)
"""

manual_test = False


def kth_min_max(arr, k):
    maxi = float("-inf")

    for num in arr:
        if num > maxi:
            maxi = num

    max_len = maxi + 1
    max_placeholder = [0] * max_len

    for num in arr:
        max_placeholder[num] += 1

    min_placeholder = max_placeholder.copy()

    max_ans = -1
    min_ans = -1

    k_max = k

    for i in range(max_len):
        if max_ans != -1 and min_ans != -1:
            break

        j = max_len - 1 - i

        if min_ans == -1:
            k -= min_placeholder[i]
            if k <= 0:
                min_ans = i
        if max_ans == -1:
            k_max -= max_placeholder[j]
            if k_max <= 0:
                max_ans = j

    return min_ans, max_ans


if __name__ == "__main__":
    arr = []
    k = 0
    if manual_test:
        size = int(input("Enter input size: "))
        k = int(input("Enter k: "))
        for i in range(0, size):
            print(f"Enter {i+1} number: ")
            arr.append(int(input()))
    else:
        # arr = [7, 10, 4, 3, 20, 15]
        # k = 3
        arr = [2, 3, 1, 20, 15]
        k = 4

    print("Array: ", arr)
    min, max = kth_min_max(arr, k)
    print(f"{k}th Min: {min} and Max: {max}")
