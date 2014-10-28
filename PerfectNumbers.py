def factors(num):
    factors = []
    for i in range(num):
        if i == 0:
            pass
        elif num % i == 0:
            factors.append(i)
    return factors


def PerfectNumber(num):
    factors_of_num = factors(num)
    if sum(factors_of_num) == num:
        return num
    else:
        return None


def main():
    print "This is a program that calculates Perfect Numbers"
    print "Press enter to keep going, and CTRL-D to stop"
    a = 2
    try:
        while True:
            x = PerfectNumber(a)
            if x is not None:
                print x
                raw_input()
            a += 1
    except EOFError:
        print "\nGood Bye!"

if __name__ == '__main__':
    main()
