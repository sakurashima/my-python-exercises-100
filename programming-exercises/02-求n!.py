# Question: Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320


def main():
    given_num = input("enter the num: ")
    sum = 1
    if(given_num == "0"):
        print("sum=0")
    else:
        for i in range(1, int(given_num)+1):
            sum *= i
        print("sum = {}".format(sum))


if __name__ == "__main__":
    main()
