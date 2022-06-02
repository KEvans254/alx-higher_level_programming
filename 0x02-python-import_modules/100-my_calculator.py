#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    o = argv[2]
    b = int(argv[3])
    i = len(argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = ["+", "-", "*", "/"]
    if o not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if o == operator[0]:
            result = add(a, b)
        elif o == operator[1]:
            result = sub(a, b)
        elif o == operator[2]:
            result = mul(a, b)
        else:
            result = div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, o, b, result))
