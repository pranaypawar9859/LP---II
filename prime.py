# Prime number checker

num = int(input("Enter a number: "))

if num > 1:
    # Assume it's prime unless proven otherwise
    is_prime = True
    
    # Check divisibility from 2 up to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, "is a Prime number")
    else:
        print(num, "is NOT a Prime number")
else:
    print(num, "is NOT a Prime number")
