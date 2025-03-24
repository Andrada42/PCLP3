def numar_vocale(s):
    ct = 0
    V = "aeiou"
    for i in s:
        if V.find(i) != -1:
            # print(f"Am gasit {i} in {s}!")
            ct += 1
    return ct

print(numar_vocale("ana are mere")) # => 6
print(numar_vocale("programarea este fun")) # => 8
print(numar_vocale("twyndyllyngs")) # => 0