#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    size = len(args) - 1

    if size != 0:
        if size == 1:
            print("{} argument:".format(size))
            print("{}: {}".format(size, args[size]))
        else:
            print("{} arguments:".format(size))
            for i in range(0, size):
                print("{}: {}".format(i, args[i]))
    else:
        print("{} arguments.".format(size))
