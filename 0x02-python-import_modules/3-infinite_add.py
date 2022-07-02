#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    args = sys.argv
    size = len(args)

    for i in range(1, size):
        result += int(args[i])
    print(result)
