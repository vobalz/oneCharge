def find_midean_2Array(A, B):
    if len(A) < len(B):
        small_array = A
        large_array = B
    else:
        small_array = B
        large_array = A
    small_min, small_max = 0, len(small_array)
    # length of array
    n, m = len(small_array), len(large_array)

    median = -1

    while small_min <= small_max:
        # small array mid index
        i = int((small_min + small_max) / 2)
        j = int((n + m + 1) / 2 - i)

        if i < n and j > 0 and small_array[i] < large_array[j - 1]:
            small_min = i + 1
        elif i > 0 and j < m and small_array[i - 1] > large_array[j]:
            small_min = i - 1
        else:
            if i == 0:
                median = large_array[j - 1]
            elif j == 0:
                median = small_array[i - 1]
            else:
                median = max(large_array[j - 1], small_array[i - 1])

            if ((n + m) % 2 == 1):
                return median

            if i == n:
                return (median + large_array[j]) / 2.0
            elif j == m:
                return (median + small_array[i]) / 2.0
            else:
                return (median + min(small_array[i], large_array[j])) / 2.0

if __name__ == '__main__':
    a = [10, 15, 23, 34]
    b = [1, 7, 12, 24, 31, 32]

    median = find_midean_2Array(a, b)
    print(median)