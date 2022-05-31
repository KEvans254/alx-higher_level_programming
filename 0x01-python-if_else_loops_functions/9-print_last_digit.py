#!/usr/bin/bash
def print_last_digit(number):
    lastDigit = str(number)[-1]
    print(f"{lastDigit:d}", end="")
    return (lastDigit)
