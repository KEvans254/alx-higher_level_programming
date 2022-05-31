#!/usr/bin/python3
def uppercase(str):
    s = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            s += chr(ord(str[i]) ^ 32)
        else:
            s += str[i]
    print(s)
