
'''
@文件    :64.py
@说明    :Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55
@时间    :2020/09/06 11:17:10
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    sum = 0

    n = int(input(""))

    for i in range(1, n+1):

        sum += i/(i+1)
        print("sum=%.2f" % sum)
        # print("i={} i+1={} i/(i+1)={}".format(i, i+1, i/(i+1)))


if __name__ == "__main__":
    main()
