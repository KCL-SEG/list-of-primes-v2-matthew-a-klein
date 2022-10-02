"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def divisible_by_any(number, list):
    return any(map(lambda y: number%y == 0, list))


def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError
    else:
        prime_list = []
        prime_list.append(2)

        primes_left = number_of_primes - 1
        number = prime_list[-1] + 1
        while primes_left > 0:

            if divisible_by_any(number, prime_list):
                number +=1
            else:
                prime_list.append(number)
                primes_left-=1


    return prime_list
