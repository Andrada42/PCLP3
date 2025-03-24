def all_combinations_target(l: list, t: int):
  # TODO 5
  sol = []
  for i1 in range(len(l)):
    for i2 in range(i1+1, len(l)):
      for i3 in range(i2+1, len(l)):
        if l[i1] + l[i2] + l[i3] == t:
          sol.append((l[i1], l[i2], l[i3]))
  return sol

print(all_combinations_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 15))