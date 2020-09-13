"""
Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
"""


def main():
    num = int(input("enter a number: "))
    num_b = num
    sum = 0
    for i in range(4):
        sum += num
        num = num*10 + num_b
    print("sum: %d" % sum)


if __name__ == "__main__":
    main()
