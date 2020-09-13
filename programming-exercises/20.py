"""
Question: Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.
"""


class NumberGenerator(object):
    def __init__(self, num_range):
        self.range = num_range

    def output(self):
        for i in range(0, self.range):
            if (i % 7 != 0):
                print(i)


def main():
    num_ger = NumberGenerator(int(input()))
    num_ger.output()

if __name__ == "__main__":
    main()
