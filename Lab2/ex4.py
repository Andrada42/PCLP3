def all_characters_strings(l: list) -> set:
    lista = []
    for stri in l:
        for c in stri:
            lista.append(c)
    # for i1 in range(len(lista)-1):
    #     for i2 in range(i1 + 1, len(lista)):
    #         if lista[i1] > lista[i2]:
    #             print(lista[i1], lista[i2])
    #             lista[i1], lista[i2] = lista[i2], lista[i1]
    #             print(lista[i1], lista[i2])
    lista.sort()
    # print (lista)
    m = set(lista)  # OBS: doar o lista/dictionar e in ordine, multimea nu poate fi sortata, e random
    return m

print(all_characters_strings(["face", "include", "flat", "banner"])) # -> {a, b, c, d, e, f, i, l, n, r, t, u}