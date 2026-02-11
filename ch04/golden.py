def golden_ratio(a, b):
    return a/b

fibNums = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
oldN = 1
for n in fibNums:
    print(golden_ratio(n, oldN))
    oldN = n


