def gcd(num1,num2):

    gcd = 0

    if num1 > num2:

        if num1 % num2 == 0:

            return num2
        
        else:

            for i in range(2,num2):

                if num1 % i == 0 and num2 % i == 0:

                    gcd = i

    elif num2 > num1:

        if num2 % num1 == 0:

            return num1
        
        else:

            for i in range(2,num1):

                if num1 % i == 0 and num2 % i == 0:

                    gcd = i

    else:

        return num1
    
    return gcd

print(gcd(18,27))