class Unique:
    def __init__(self, items, ignore_case=False, **kwargs):
        self.items = items
        self.ignore_case = ignore_case
        self.set = set()
        self.index = 0

    def __next__(self):
        # Если игнорируем верхний регистр, то пробегаемся по списку и приводим всё к нижнему регистру.
        if self.ignore_case:
            for i, elem in enumerate(self.items):
                if type(elem) is str:
                    self.items[i] = elem.lower()
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            else:
                current = self.items[self.index]
                self.index += 1
                # если текущего числа ещё не было, добавляем и возвращаем.
                if current not in self.set:
                    self.set.add(current)
                    return current

    def __iter__(self):
        return self