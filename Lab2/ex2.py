def reverse_tuple(t: tuple) -> tuple:
  # TODO 2
  newtuple = t[::-1]
  # OBS: daca t era [1, 3, 5, 10] atunci newtuple era tot o lista
  return newtuple

print(reverse_tuple((1, 3, 5, 10))) # => [(10, 5, 3, 1)]