def sort_tuple_list(l: list):
  newlist = []
  for tupleindex in range(len(l)-1):
    # print(tupleindex, l[tupleindex])
    for tupleindex2 in range(tupleindex + 1, len(l)):
        # print(tupleindex2, l[tupleindex2])
        if l[tupleindex][0] > l[tupleindex2][0]:
           val1 = l[tupleindex]
           val2 = l[tupleindex2]
           l[tupleindex] = val2
           l[tupleindex2] = val1
        elif l[tupleindex][0] == l[tupleindex2][0] and l[tupleindex][1] < l[tupleindex2][1]:
            val1 = l[tupleindex]
            val2 = l[tupleindex2]
            l[tupleindex] = val2
            l[tupleindex2] = val1
  return l

print(sort_tuple_list([(3, 1), (2, 2)]))  # => [(2, 2), (3, 1)]
print(sort_tuple_list([(0, 3), (3, 1), (2, 4), (10, 2), (1, 2), (0, 5)]))  # =>  [(0, 5), (0, 3), (1, 2), (2, 4), (3, 1), (10, 2)]
print(sort_tuple_list([(5, 6), (1, 3), (10, 5), (9, 1), (5, 7)]))  # =>  [(1, 3), (5, 7), (5, 6), (9, 1), (10, 5)]