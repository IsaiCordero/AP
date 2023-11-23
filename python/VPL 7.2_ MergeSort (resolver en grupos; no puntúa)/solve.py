def solve(items):
    """
    Sort the given list of items in ascending order
    """

    def merge(left, mid, right):
        # solve it here!
        A = items[left:]
        B = items[:right]
        result = [0] * len(items)
        i = 0
        j = 0
        for k in range(0, len(items)):
            if i < len(A) and (j == len(B) or A[i] <= B[j]):
                items[k] = A[i]
                i += 1
                continue
            if j < len(B) and (i == len(A) or B[j] < A[i]):
                items[k] = B[j]
                j += 1
                continue
            else:
                return result

        ...

    def merge_sort(left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid + 1, right)
        # solve it here!
        ...

    merge_sort(0, len(items) - 1)
    return
