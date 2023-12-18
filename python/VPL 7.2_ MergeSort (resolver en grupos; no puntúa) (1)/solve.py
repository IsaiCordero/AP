
def solve(items):
    """
    Sort the given list of items in ascending order
    """

    def merge(left, mid, right):
        izquierda = items[left:mid + 1]
        derecha = items[mid + 1:right + 1]

        i = j = 0
        k = left
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                items[k] = izquierda[i]
                i += 1
            else:
                items[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            items[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            items[k] = derecha[j]
            j += 1
            k += 1

    def merge_sort(left, right):
        if left < right:
            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            merge(left, mid, right)


    merge_sort (0, len(items)-1)
    return items
