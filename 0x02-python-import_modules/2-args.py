#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys
    total = len(sys.argv) - 1
    if total == 0:
        print("0 argument.")
    elif total == 1:
        print("1 argument:")
    else:
        print("{}argument:".format(total))
    for e in range(total):
        print("{}: {}".format(e + 1, sys.argv[e + 1]))
