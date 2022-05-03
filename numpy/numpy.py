import numpy as np

# 1
arr1 = np.outer(np.arange(1, 11, 1), np.arange(1, 11, 1))
print("arr1:", arr1, "\n")

# 2
arr2 = arr1[3:7, 3:7]
print("4x4 inside arr1 (arr2):", arr1[3:7, 3:7], "\n")

# 3
arr3 = np.arange(1, 17, 1)
arr3 = arr3.reshape(4,4)
print("arr3 reshaped:", arr3, "\n")

# 4
arr4 = (arr2 % 2 == 0) & (arr3 % 2 == 0)
print("arr4:", arr4, "\n")

# 5
print("even #s in arr2:", arr2[arr2 % 2 == 0].size, "\n")

# 6
print("square root of arr3:", np.sqrt(arr3), "\n")

# 7
arr7 = np.zeros(arr1.shape)
np.fill_diagonal(arr7, 1)

arr7 = arr1 + arr7
print("arr7:", arr7, "\n")

# 8
print("arr1 flipped on 0 and 1 axis:", np.flip(arr1, (0, 1)), "\n")

# 9
arr9 = np.random.random((10, 10)) * 10
print("arr9 (sorted):", np.sort(arr9), "\n")

# 10
arr10 = np.average(arr1, 0)
print("arr1 average value per row:", np.vstack(arr10), "\n")

# 11
def mergeSort(arr):
    if arr.size > 1:
        arr = np.hstack(arr)

        middle = arr.size // 2
        Left, Right = np.array_split(arr, 2)

        mergeSort(Left)
        mergeSort(Right)

        i = j = k = 0

        while i < Left.size and j < Right.size:
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while i < Left.size:
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < Right.size:
            arr[k] = Right[j]
            j += 1
            k += 1

        return arr

arr11 = mergeSort(arr1)
print("mergeSorted array (arr11):", arr11, "\n")