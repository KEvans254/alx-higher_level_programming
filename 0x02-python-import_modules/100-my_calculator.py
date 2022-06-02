#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = sys.argv[1]
    o = sys.argv[2]
    b = sys.argv[3]
    i = len(sys.argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = ["+", "-", "*", "/"]
    if o not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if o == operator[0]:
            print("{} {} {} = {}".format(a, o, b, add(int(a), int(b))))
        elif o == operator[1]:
            print("{} {} {} = {}".format(a, o, b, sub(int(a), int(b))))
        elif o == operator[2]:
            print("{} {} {} = {}".format(a, o, b, mul(int(a), int(b))))
        else:
            print("{} {} {} = {}".format(a, o, b, div(int(a), int(b))))
