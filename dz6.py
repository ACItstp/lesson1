result = []

def divider(a, b):
    if a < b:
        raise ValueError("a < b")

    if b > 100:
        raise IndexError("b > 100")

    return a / b


data = [
    (10, 2),
    (2, 5),
    ("123", 4),
    (18, 0),
    ([1, 2], 15),
    (8, 4)
]

for a, b in data:
    try:
        res = divider(a, b)
        result.append(res)

    except Exception as e:
        print(type(e).__name__, "-", e)

print("Результат:", result)
