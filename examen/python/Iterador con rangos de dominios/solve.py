class My_Iterator:
    def __init__(self, num_digits, min_values, max_values):
        self.num_digits = num_digits
        self.min_values = min_values
        self.max_values = max_values
        self.current = [min_values[i] for i in range(self.num_digits)]

    def incremento(self):
        i = self.num_digits - 1
        while i >= 0:
            self.current[i] += 1
            if self.current[i] <= self.max_values[i]:
                break
            self.current[i] = self.min_values[i]
            i -= 1
        return i >= 0

    def next(self):
        while True:
            yield list(self.current)
            if not self.incremento():
                break
