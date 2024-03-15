#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count_argv = len(sys.argv) - 1
    if count_argv == 0:
        print("0 arguments.")
    elif count_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count_argv))
    for i in range(count_argv):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

