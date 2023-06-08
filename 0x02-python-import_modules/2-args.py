#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    print("{} ".format(args - 1), end="")
    if num == 1:
        print("arguments.")
    elif num > 1:
        if num == 2:
            print("argument:")
        elif num > 2:
            print("arguments:")
        for i in range(args - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
