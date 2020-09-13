"""
Question: Write a program that accepts a comma separated sequence of words as input and prints the words 
in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied 
to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world
"""
def main():
    strs_list = [x for x in input().split(",")]
    strs = sorted(strs_list)



if __name__ == "__main__":
    main()