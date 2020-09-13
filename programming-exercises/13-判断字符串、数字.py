"""
Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: 
LETTERS 10 DIGITS 3
"""


def main():
    input_strs = input("enter a sentence: ")
    mydict = {"LETTERS": 0, "DIGITS": 0}  # 使用字典来储存数据

    for i in input_strs:
        if i.isalpha():
            mydict["LETTERS"] += 1
        if i.isdigit():
            mydict["DIGITS"] += 1

    print("LETTERS: {}, DIGITS:{}".format(mydict["LETTERS"], mydict["DIGITS"]))



if __name__ == "__main__":
    main()
