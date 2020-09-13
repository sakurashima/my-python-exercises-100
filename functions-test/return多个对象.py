from operator import itemgetter


def itemgetter(a, b, c):
    return a, b, c


def main():
    mytuple = (1, 2, 3)
    a, b, c = itemgetter(mytuple[0], mytuple[1], mytuple[2])
    print(a, b, c)


if __name__ == "__main__":
    main()
