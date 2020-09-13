# Question: Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

def main():

    num_strs = input("enter the nums:")
    num_list = num_strs.split()  #split方法用来切割字符串，有两个参数
    print(num_list)
    print(tuple(num_list))


if __name__ == "__main__":
    main()
