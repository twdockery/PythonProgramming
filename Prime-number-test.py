def is_prime(num):
    factor = num
    for i in range(1,num):
        num -= 1
        if factor % num == 0:
            print("This number is NOT prime. %s is a factor of %s" % (num, factor))
            break
        else:
            if num == 1:
                print("This number is a PRIME")

is_prime(int(input("what is your number: ")))