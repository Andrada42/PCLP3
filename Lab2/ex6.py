# Ana are mere, pere, si caise. Dar mere are multe. Mere.

sir = input()
sir = sir.replace(",","")
sir = sir.replace(".","")
sir = sir.lower()
cuvinte = sir.split(" ")

dictionar = {}
for cuv in cuvinte:
    if cuv in dictionar:
        nr = dictionar[cuv] + 1
    else:
        nr = 1
    dictionar.update({cuv: nr})

# print(sir)
# print(cuvinte)
# print(dictionar)