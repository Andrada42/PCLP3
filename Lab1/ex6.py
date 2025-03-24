def afisare_progresie_aritmetica(start, stop, pas = 2):
  # TODO 6
  for i in range(start, stop, pas):
    print(i, end=' ')
  print(end="\n")
  pass

afisare_progresie_aritmetica(1, 50, 5)
afisare_progresie_aritmetica(-5, 25)