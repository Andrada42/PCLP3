def concatenare_cuvinte(*args):
  # TODO 5
  for i in args:
    if isinstance(i, str):
        list.append(i)
  s=" ".join(list)
  return s

print(concatenare_cuvinte("ana", "are", 2, "mere"))
print(concatenare_cuvinte("programarea", "calculatoarelor", "si", "limbaje", "de", "programare", 3))