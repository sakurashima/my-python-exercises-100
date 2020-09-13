
def main():
    x = int(input("x:"))
    y = int(input("y:"))
    # for i in range(0, x):
    #     for j in range(0, y):
    #         print(i*j, end=",")
    #     print("")
    two_dimentions_num_lists = [[0 for i in range(y)] for j in range(x)]
    print(two_dimentions_num_lists)


    for i in range(x):
        for j in range(y):
            two_dimentions_num_lists[i][j] = i*j
    print(two_dimentions_num_lists)


if __name__ == "__main__":
    main()
