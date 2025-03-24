import string

def transforma_cuvinte(s):
    s = string.capwords(s)
    return s

print(transforma_cuvinte("Ana are mere"))
print(transforma_cuvinte("programarea calculatoarelor si limbaje de programare trei"))