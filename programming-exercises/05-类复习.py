# Question: Define a class which has at least two methods:
# getString: to get a string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints: Use init method to construct some parameters

class MyClass:
    def __init__(self, str):
        self.str = str

    def getString(self):
        print(self.str.upper())


def main():
    mystr = input("enter the string:")
    mystrclass = MyClass(mystr)
    mystrclass.getString()


if __name__ == "__main__":
    main()
