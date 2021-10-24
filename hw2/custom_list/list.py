class CustomList(list):

    def __init__(self, *args):
        super().__init__(args)

    def __add__(self, other):
        res = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            res.append((self[i] if i < len(self) else 0) + (other[i] if i < len(other) else 0))
        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        max_len = max(len(self), len(other))
        for i in range(max_len):
            if i >= len(self):
                self.append(other[i])
            else:
                self[i] = self[i] + (other[i] if i < len(other) else 0)
        return self

    def __sub__(self, other):
        res = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            res.append((self[i] if i < len(self) else 0) - (other[i] if i < len(other) else 0))
        return res

    def __rsub__(self, other):
        res = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            res.append((other[i] if i < len(other) else 0) - (self[i] if i < len(self) else 0))
        return res

    def __isub__(self, other):
        max_len = max(len(self), len(other))
        for i in range(max_len):
            if i >= len(self):
                self.append(0 - other[i])
            else:
                self[i] = self[i] - (other[i] if i < len(other) else 0)
        return self

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
