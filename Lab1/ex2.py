def cifra_maxima(n):
    c = 0
    currentc = 0
    while n != 0:
        currentc = n % 10
        if c < currentc:
            c = currentc
        n = n // 10
    return c

print(cifra_maxima(1234567)) # => 7
print(cifra_maxima(123984)) # => 9
print(cifra_maxima(2222)) # => 2
print(cifra_maxima(1)) # => 1
