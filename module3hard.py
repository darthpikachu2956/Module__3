data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    summa = 0
    for i in data:
        if isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, dict):
            summa += sum(i.values())
            summa += sum(len(key) for key in i.keys())
        elif isinstance(i, (tuple, set, list)):
            summa += calculate_structure_sum(i)
    return summa


summa = calculate_structure_sum(data_structure)
print(summa)
