"""
Question: Write a program to compute the frequency of the words from the input. The output should output 
after sorting the key alphanumerically. Suppose the following input is supplied to the program: 
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. 
Then, the output should be: 
2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

"""


def main():

    input_dict = dict()
    input_strs = input().split(" ")

    # 利用集合去除重复的元素
    input_set = set(input_strs)

    # 创建字典
    for i in input_set:
        input_dict[i] = 0

    # 遍历字符串，如果遇到相同元素，数量加一到字典里面
    for i in input_strs:
        input_dict[i] += 1

    # print(input_dict)
    ret_list = list()
    for i in input_dict:
        ret_list.append((i+":"+str(input_dict[i])))

    print(" ".join(sorted(ret_list)))


if __name__ == "__main__":
    main()
