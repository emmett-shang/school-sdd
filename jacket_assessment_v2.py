import random  # import the libary, random

import time  # import the library, time




clothes_list = []  # placeholder/empty list for later use


def rejected():
    category = "rejected"
    graded = "N/A"

    return category, graded


def small(grade):
    graded = ""

    category = "small"

    if grade.lower() == "j":  # junior

        graded = "junior"

    elif grade.lower() == "s":  # senior
        graded = "senior"

    return category, graded


def medium(grade):
    graded = ""

    category = "medium"
    if grade.lower() == "j":  # junior

        graded = "junior"

    elif grade.lower() == "s":  # senior
        graded = "senior"

    return category, graded


def large(grade):
    graded = ""

    category = "large"
    if grade.lower() == "j":  # junior

        graded = "junior"

    elif grade.lower() == "s":  # senior
        graded = "senior"
    return category, graded


def jacket_sorter_manual():  # clothes_sorter function

    while True:
        size = input("input the size of the jacket into the system: ")  # ask for size input for clothes

        if size.isdigit():  # checks if the input can be converted to integer
            size = int(size)  # converts size into integer
            grade = input("Junior(j) or Senior(s)? ")  # ask for the grade of clothes, whether its junior or senior
            if grade.lower() == "j" or grade.lower() == "s":  # checks for valid input
                match size:
                    case _ if size < 5:
                        print("size and grade: " + str(rejected()))  # rejected
                        clothes_final = (
                            size, *rejected()
                        )  # adds all the values including size, category and grade into a variable
                        clothes_list.append(clothes_final)
                        print("-------------------------------")

                    case _ if 5 <= size <= 10:
                        print("size and grade: " + str(small(grade)))
                        clothes_final = (
                            size, *small(grade)
                        )  # adds all the values including size, category and grade into a variable
                        clothes_list.append(clothes_final)
                        print("-------------------------------")

                    case _ if 10 < size <= 20:
                        print("size and grade: " + str(medium(grade)))
                        clothes_final = (
                            size, *medium(grade))  # adds all the values including size, category and grade into a variable
                        clothes_list.append(clothes_final)
                        print("-------------------------------")

                    case _ if size > 20:
                        print("size and grade: " + str(large(grade)))
                        clothes_final = (
                            size, *large(grade))  # adds all the values including size, category and grade into a variable
                        clothes_list.append(clothes_final)
                        print("-------------------------------")

                # adds clothes_final values to the list clothes_list
            else:  # returns a message for invalid input of grade
                print("This is not a valid grade")
                continue  # skips to the next iteration of the loop
        else:  # returns a message for invalid input of size
            print("This is not a valid size")
            continue  # skips to the next iteration of the loop

        proceed = input("do you want to continue y/n: ")  # asks if the user wants to continue manual input

        if proceed.lower() == "y":  # if input is "y" or "Y"
            pass  # continue to the next step of the loop
        elif proceed.lower() == "n":  # if input is "n" or "N"
            break  # stop the current loop
        else:  # else if the input is invalid, automatically stop the loop
            print("Invalid input. Auto stopping manual input...")
            break


def rejected_auto():
    category = "rejected"
    grade = "N/A"

    return category, grade
def small_auto():

    category = "small"

    if random.random() <= 0.75:  # returns a random value between 0 and 1. If the value is below 0.75 grade = Junior making it a 75% chance
        grade = "junior"

    else:  # else returns senior grade
        grade = "senior"

    return category, grade

def medium_auto():
    category = "medium"
    if random.random() <= 0.5:  # if the value is below 0.5, grade = junior (50% chance)
        grade = "junior"

    else:  # else grade = senior
        grade = "senior"

    return category, grade

def large_auto():

    category = "large"

    if random.random() <= 0.25:  # if the value is below 0.25, grade = junior (25% chance)
        grade = "junior"

    else:  # else grade = senior
        grade = "senior"

    return category, grade

def jacket_sorter_auto():
    grade = ""
    num = input("How many clothes would you like to sort: ")  # retrives input for number of clothes you want to input

    if num.isdigit():  # checks if "num" can be converted to an integer
        for i in range(int(num)):  # loop "num" amount of times
            size_auto = random.randint(0, 30)  # generate a random clothes size between 0 and 30

            match size_auto:

                case _ if size_auto < 5:
                    print(f"Weight of clothes: {size_auto}")
                    print("size and grade: " + str(rejected_auto()))
                    print("-------------------------------")
                    clothes_final = (size_auto, *rejected_auto())  # assigns or the values including size of clothes, category and grade to a variable
                    clothes_list.append(clothes_final)

                    time.sleep(1)  # delay for 1 second
                case _ if 5 <= size_auto <= 10:
                    print(f"Weight of clothes: {size_auto}")
                    print("size and grade: " + str(small_auto()))
                    print("-------------------------------")
                    clothes_final = (size_auto, *small_auto())  # assigns or the values including size of clothes, category and grade to a variable
                    clothes_list.append(clothes_final)
                    time.sleep(1)
                case _ if 10 < size_auto <= 20:  # medium
                    print(f"Weight of clothes: {size_auto}")
                    print("size and grade: " + str(medium_auto()))
                    print("-------------------------------")
                    clothes_final = (size_auto, *medium_auto())  # assigns or the values including size of clothes, category and grade to a variable
                    clothes_list.append(clothes_final)
                    time.sleep(1)
                case _ if size_auto < 20:  # large
                    print(f"Weight of clothes: {size_auto}")
                    print("size and grade: " + str(large_auto()))
                    clothes_final = (size_auto, *large_auto())  # assigns or the values including size of clothes, category and grade to a variable
                    clothes_list.append(clothes_final)
                    print("-------------------------------")
                    time.sleep(1)

              # adds clothes_final values to the list clothes_list
    else:  # if num cannot be converted to an integer return error message
        print("Invalid input")
        pass  # loop continues to the next step


def repeat_sorter():
    while True:
        mode = input(
            "do you want manual(m) or automatic(a) mode or are you done(d): ")  # input for the mode option either manual mode, automatic mode or exiting and ending the program
        match mode:

            case _ if mode.lower() == "m":  # checks if the mode is manual (keyword it is looking for is m). .lower() makes it so that it is not case sensitive
                jacket_sorter_manual()
            case _ if mode.lower() == "a":  # else if the mode input is "a" or "A"
                jacket_sorter_auto()
            case _ if mode.lower() == "d":  # if mode input = "d" or "D"
                print("clothes sorter shutting down...")
                print("-------------------------------")
                break

            case _:  # else if the mode input is none of the above return an error message
                print("Input is invalid. Please input a valid option")
                print("-------------------------------")

    if len(clothes_list) == 0:
        print("Why did you even turn on the sorter?")

    print("All the sorted clothes in your session: \n" + str(clothes_list))


def main():
    repeat_sorter()


if __name__ == "__main__":
    main()
