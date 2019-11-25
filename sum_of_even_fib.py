#Sum of even Fibinocci numbers till 4000000

def sum_of_even_fib(num) :
    '''this method returns the sum of the even fibinocci numbers till the num'''
    m, n = 0, 1
    total = 0
    while n < num :
        if n%2 == 0 :
            total = total + n
        m, n = n, m+n
    return total

print(sum_of_even_fib(4000000))
