#Multiples of 3 and 5

def multiples_of_3_and_5(num) :
    ''' This method returns all the multiples of 3 and 5 below the number num'''
    multiples_of_3 = []
    multiples_of_5 = []
    m, index1 = 3, 1
    n, index2 = 5, 1

    while (m < num) :
        multiples_of_3.append(m)
        index1 += 1
        m = 3*index1
    while (n < num) :
        multiples_of_5.append(n)
        index2 += 1
        n = 5*index2
    #print (multiples_of_5, multiples_of_3)
    return sum(list(set(multiples_of_5).union(set(multiples_of_3))))

print(multiples_of_3_and_5(1000))