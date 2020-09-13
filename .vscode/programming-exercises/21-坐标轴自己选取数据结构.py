"""
Question A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, 
DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 
3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program to compute the 
distance from current position after a sequence of movement and original point. If the distance is a 
float, then just print the nearest integer. Example: If the following tuples are given as input to the 
program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2
"""
import math


def main():

    position = {"x": 0, "y": 0}

    while True:
        my_str = input()
        if not my_str:
            break
        my_str = my_str.split(" ")

        direction = my_str[0]        # 方向
        distance = int(my_str[1])    # 距离

        if direction == "UP":
            position["y"] += distance
        elif direction == "DOWN":
            position["y"] -= distance
        elif direction == "RIGHT":
            position["x"] += distance
        elif direction == "LEFT":
            position["x"] -= distance

    ret = int(position["x"])**2 + int(position["y"])**2
    ret = math.sqrt(ret)
    print(round(ret))


if __name__ == "__main__":
    main()
