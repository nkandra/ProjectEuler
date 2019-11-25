#finding the largest prime factor of a number

def largest_prime_factor(num) :
    factors = set()
    while (num%2 == 0) :
        factors.add(2)
        num = num//2
    f = 3
    num1 = num
    while (f*f < num1) :
        #print(num)
        if num%f == 0 :
            factors.add(f)
            num = num//f
        f = f+2
    #print(factors)
    return max(factors)

print(largest_prime_factor(600851475143))