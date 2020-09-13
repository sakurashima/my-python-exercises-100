"""
Question: Write a program that calculates and prints the value according to the given formula: 
Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. 
D is the variable whose values should be input to your program in a comma-separated sequence. 
Example Let us assume the following comma separated input sequence is given to the program: 
100,150,180 The output of the program should be: 18,22,24
"""


def num_handle(num):
    sum = (2*50*num)/30
    for i in range(1, num):
        if i*i < sum and (i+1)*(i+1) > sum:
            return i


def main():
    
    outPut_num_list = list()
    num_D = input("enter the D:")

    num_D_list = num_D.split(",")

    for i in num_D_list:
        # print(i)
        outPut_num_list.append(str(num_handle(int(i))))

    print(",".join(outPut_num_list))


if __name__ == "__main__":
    main()
