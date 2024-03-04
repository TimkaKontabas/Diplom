row = [1, 2, 3, 4, 5, 6, 7, 8]
d = [row[i:i+2] for i in range(0, len(row), 2)]
print(d)