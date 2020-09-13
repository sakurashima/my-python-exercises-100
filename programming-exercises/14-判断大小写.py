"""
Question: Write a program that accepts a sentence and calculate the number of upper case letters and 
lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the 
output should be: UPPER CASE 1 LOWER CASE 9
"""


def main():
    mydict = {"UPPER CASE": 0, "LOWER CASE": 0}
    words = input("enter a sentence: ")

    for word in words:
        if word.isupper():
            mydict["UPPER CASE"] += 1
        if word.islower():
            mydict["LOWER CASE"] += 1
    print("UPPER CASE: {}, LOWER CASE: {}".format(mydict["UPPER CASE"],  mydict["LOWER CASE"]))

if __name__ == "__main__":
    main()
