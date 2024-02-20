n, i, j = map(int, input().split())

dist1 = abs(j - i) - 1  # Расстояние по часовой стрелке. Учитываем два сл-я i < j, i > j
dist2 = n - 2 - dist1  # Расстояние против часовой стрелки
print(min(dist1, dist2))
