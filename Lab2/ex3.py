def all_tuple_exist(l: list, element) -> bool:
  # TODO 3
  
  for x in l:
    # print(x)
    gasit = 0

    # Metoda 1
    # for e in x:
    #     if e == element:
    #        gasit = 1
    #        break

    # Metoda 2
    if element in x:
       gasit = 1
    
    if gasit == 0:
        return False
    
  return True

print(all_tuple_exist([(1, 4, 2, 3), (10, 11, 2, 3), (6, 7, 1)], 2)) # -> False
print(all_tuple_exist([("string", 2, -1), (-10, 5, "string", 1, -1.3), (2, "string", -0.5, 2)], "string")) # -> True