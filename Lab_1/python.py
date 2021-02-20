from math import*
from random import*
import sys

def try_parse_int(str): ## checking if value acceptable to be parsed to integer
    try:
        return int(str)
    except ValueError:
        return None

def try_parse_float(str): ## checking if value acceptable to be parsed to float
    try:
        return float(str)
    except ValueError:
        return None


print(''.join('=') * 80) ## just decor

choose = input("What you want to see? ('1' - for part 1, '2' - for part 2, '3' - for part 3) - ")
choose = try_parse_int(choose)

print(''.join('=') * 80)

if choose == 1:

    ## Part 1 ##

    print(''.join('=') * 20)
    print('Part 1')
    print(''.join('-') * 20)    

    #########################   

    a = input('Enter a: ')
    b = input('Enter b: ')  

    print(''.join('-') * 20)

    a = try_parse_float(a)
    b = try_parse_float(b)    

    if a == None or b == None:

        print(''.join('~') * 45)
        print('Wrong input, a and b must be float number')
        print(''.join('~') * 45)
    
    else:

        z = 0.0 

        if a >= 15:

            z = sin(2 * a) + cos(2 * b)

        else:

            if (a + pow(b, 2)) <= 0:

                print(''.join('~') * 55)
                print('Error calculation, please be sure, that a + b^2 > 0')
                print(''.join('~') * 55)
            
            else:    
                
                z = sqrt(a + pow(b, 2)) 

        if z != 0:

            print('Result of function = ', z)   

    #########################   

    print(''.join('-') * 20)
    print('End of part 1')
    print(''.join('=') * 20)    

    ## End of Part 1 ##

elif choose == 2:

    ## Part 2 ##

    print(''.join('=') * 20)
    print('Part 2')
    print(''.join('-') * 20)    

    #########################   

    n = input('Enter natural value of n: ')
    n = try_parse_int(n) 

    print(''.join('-') * 20) 

    if n == None or n <= 0:

        print(''.join('~') * 45)
        print('Wrong input, n must be natural integer number')
        print(''.join('~') * 45)
    
    else:

        z = 0.0 

        for i in range(1, n + 1):
            z = z + (i + 1) / i 

        print('Result of sequence = ', z)   

    #########################   

    print(''.join('-') * 20)
    print('End of part 2')
    print(''.join('=') * 20)    

    ## End of Part 2 ##

elif choose == 3:

    ## Part 3 ##

    print(''.join('=') * 20)
    print('Part 3')
    print(''.join('-') * 20)    

    #########################   

    N = input('Enter length N: ')

    print(''.join('-') * 20) 
    
    N = try_parse_int(N)  

    if N == None or N <= 0:

        print(''.join('~') * 45)
        print('Wrong input, N must be natural integer number')
        print(''.join('~') * 45)
        print(''.join('=') * 80)
    
    else:

        massive = []
        massiveOfNegative = []
        max = -inf
        sumOfPaired = 0 

        for i in range(N):
            randomValue = randrange(-99, 99)
            massive = massive + [randomValue]

            if max < randomValue:
                max = randomValue

            if randomValue % 2 == 0:
                sumOfPaired = sumOfPaired + randomValue  

            if randomValue < 0:
                massiveOfNegative = massiveOfNegative + [randomValue]    

        print("Massive: ", massive)
        print(''.join('-') * 20)

        print('Results:')
        print(''.join('-') * 20)

        print('Max value = ', max)  

        print('Sum of paired elements = ', sumOfPaired) 

        print('Reverse list of negative: ', massiveOfNegative[::-1])     

        #########################   

        print(''.join('-') * 20)
        print('End of part 3')
        print(''.join('=') * 20)    

        ## End of Part 3 ##

else:

    print(''.join('~') * 65)
    print("Wrong input choosing part (acceptable variants: '1' or '2' or '3')")
    print(''.join('~') * 65)
    print(''.join('=') * 80)