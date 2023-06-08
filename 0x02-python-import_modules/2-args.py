#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    print("{} ".format(args - 1), end="")
    if args == 1:
        print("1")
    elif args > 1:
        if args == 2:
            print("2")
        elif args > 2:
            print("arguments:")
        for x in range(args - 1):
            print("{}: {}".format((x + 1), sys.argv[x + 1]))
