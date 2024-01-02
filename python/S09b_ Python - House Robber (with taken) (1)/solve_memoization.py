def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        if n < 0:
            return 0
        if n in mem:
            return mem[n]

        mem[n] = max(t(n - 2) + items[n], t(n - 1))
        return mem[n]

    def fill_taken():
        nonlocal taken
        i = len(items) - 1
        while i >= 0:
            if i == 0:
                taken.append(i)
                break
            if mem[i] == mem[i - 1]:
                i -= 1
            else:
                taken.append(i)
                i -= 2
        taken.reverse()

    n = len(items) - 1
    max_benefit = t(n)
    fill_taken()

    return max_benefit, taken
