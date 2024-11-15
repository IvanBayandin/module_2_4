numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'numbers = {numbers}')
primes = []
not_primes = []

for i in range(len(numbers)+1):
    is_prime = True
    if i <= 1: #пропускаем 0 и 1
        continue
    else:
        for j in range(2, int(i ** 0.5) + 1): #корень квадратный
            if i % j == 0:
                is_prime = False
                break
        if not (is_prime):
            not_primes.append(i)
        else:
            primes.append(i)
print(f'Primes: {primes}')
print(f'Not_primes: {not_primes}')
