def primes(max):
    if max <= 1:
        return []
    else:
        primes_number = [2]
        for i in range(3, max+1):
            is_prime = True
            for div in primes_number:
                if i % div == 0:
                    is_prime = False
                    break
            if is_prime == True:
                primes_number.append(i)
        return primes_number
