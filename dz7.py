class PowerOfTwo:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = 2 ** self.n
        self.n += 1
        return value


it = PowerOfTwo()

for _ in range(6):
    print(next(it))
