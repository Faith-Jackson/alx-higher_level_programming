#!/usr/bin/python3
""" prints the number of and the list of its arguments."""
if __name__ == "__main__":
    import sys

    arg = sys.argv
    num_argv = len(arg) - 1

    if num_argv > 1:
        print("{} arguments:".format(num_argv))
        for i in range(1, num_argv + 1):
            print("{}: {}".format(i, arg[i]))

    elif num_argv == 0:
        print("{} arguments.".format(num_argv))

    else:
        print("{} argument:".format(num_argv))
        print("{}: {}".format(num_argv, arg[1]))
