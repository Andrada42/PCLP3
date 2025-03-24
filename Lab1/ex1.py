def suma_cifre(n):
    s = 0
    while n != 0:
        s = s + n % 10
        n = n // 10
    return s

print(suma_cifre(123))
print(suma_cifre(2222))
print(suma_cifre(32145))