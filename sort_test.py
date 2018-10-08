from sys import argv
import sort

if __name__ == '__main__':
    arr = []
    try:
        arr = list(argv[1].split(","))
        for e in range(0, len(arr)):
            arr[e] = int(arr[e])
    except (IndexError, TypeError, ValueError):
        print("Incorrect input args")
        exit(1)
    try:
        sort.quick_sort(arr)
    except TypeError as e:
        print(repr(e))
        exit(1)
    print(arr)
