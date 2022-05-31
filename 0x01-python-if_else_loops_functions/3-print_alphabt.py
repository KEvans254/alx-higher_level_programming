#!/usr/bin/python3
for ch in range(97, 123):
    if (f"{ch:c}") != "q" and (f"{ch:c}") != "e":
        print(f"{ch:c}", end="")
