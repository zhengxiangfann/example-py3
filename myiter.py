


class Data(object):

    def __init__(self):
        self._data = []

    def add(self, x):
        self._data.append(x)

    def data(self):
        return iter(self._data)


# 标准的迭代器


class Data(object):
    def __init__(self, *args):
        self._data = list(args)
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data[self._index]
        self._index += 1
        return d


d = Data(1, 2, 3)
for x in d:
    print(x)
