class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.lift_up(self.size - 1)

    def lift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]

    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.lift_down(self.values[0])
        return tmp

    def lift_down(self, i):
        while (2 * i) + 1 < self.size:
            j = i
            if self.values[(2 * i) + 1] < self.values[i]:
                j = (2 * i) + 1
            if (2 * i) + 2 < self.size and self.values[(2 * i) + 2] < self.values[j]:
                j = (2 * i) + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
