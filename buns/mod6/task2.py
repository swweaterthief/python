class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.index = 0

    def __next__(self):
        if self.index < len(self.lst):
            pair = (self.lst[self.index], self.lst[self.index + 1] if self.index + 1 < len(self.lst) else None)
            self.index += 2
            return pair
        else:
            raise StopIteration

    def __iter__(self):
        return self