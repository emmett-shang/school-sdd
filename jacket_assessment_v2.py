import random  # import the libary, random

import time  # import the library, time

clothes_list = []  # placeholder/empty list for later use


def jacket_sorter_manual():  # clothes_sorter function

    while True:
        size = input("input the size of the jacket into the system: ")  # ask for size input for clothes

        if size.isdigit():  # checks if the input can be converted to integer
            size = int(size)  # converts size into integer
            grade = input("Junior(j) or Senior(s)? ")  # ask for the grade of clothes, whether its junior or senior
            if grade.lower() == "j" or grade.lower() == "s":  # checks for valid input
                if size < 5:  # rejected
                    category = "rejected"
                    print(category)
                    grade = "N/A"
                    print("grade: " + grade)
                    print("-------------------------------")
                elif 5 <= size <= 10:  # small
                    print("accepted")
                    category = "small"
                    print("size: " + category)

                    if grade.lower() == "j":  # junior

                        grade = "junior"
                        print("grade: " + grade)
                    elif grade.lower() == "s":  # senior
                        grade = "senior"
                        print("grade: " + grade)

                    print("-------------------------------")
                elif 10 < size <= 20:  # medium
                    print("accepted")
                    category = "medium"
                    print("size: " + category)
                else:  # large
                    print("accepted")
                    category = "large"
                    print("size: " + category)

                    print("-------------------------------")

                clothes_final = (
                    size, category, grade)  # adds all the values including size, category and grade into a variable
                clothes_list.append(clothes_final)  # adds clothes_final values to the list clothes_list
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


def jacket_sorter_auto():
    grade = ""
    num = input("How many clothes would you like to sort: ")  # retrives input for number of clothes you want to input
    if num.isdigit():  # checks if "num" can be converted to an integer
        for i in range(int(num)):  # loop "num" amount of times
            size_auto = random.randint(0, 30)  # generate a random clothes size between 0 and 30
            print(f"Weight of clothes: {size_auto}")
            if size_auto < 5:  # rejected
                category = "rejected"
                print(category)
                print("-------------------------------")

                time.sleep(1)  # delay for 1 second
            elif size_auto >= 5 and size_auto <= 10:  # small
                print("accepted")
                category = "small"
                print("size: " + category)
                if random.random() <= 0.75:  # returns a random value between 0 and 1. If the value is below 0.75 grade = Junior making it a 75% chance
                    grade = "junior"
                    print("grade: " + grade)
                else:  # else returns senior grade
                    grade = "senior"
                    print("grade: " + grade)
                print("-------------------------------")

                time.sleep(1)
            elif size_auto > 10 and size_auto <= 20:  # medium
                print("accepted")
                category = "medium"
                print("size: " + category)
                if random.random() <= 0.5:  # if the value is below 0.5, grade = junior (50% chance)
                    grade = "junior"
                    print("grade: " + grade)
                else:  # else grade = senior
                    grade = "senior"
                    print("grade: " + grade)
                print("-------------------------------")

                time.sleep(1)
            else:  # large
                print("accepted")
                category = "large"
                print("size: " + category)
                if random.random() <= 0.25:  # if the value is below 0.25, grade = junior (25% chance)
                    grade = "junior"
                    print("grade: " + grade)
                else:  # else grade = senior
                    grade = "senior"
                    print("grade: " + grade)
                print("-------------------------------")
                time.sleep(1)
            clothes_final = (size_auto, category,
                             grade)  # assigns or the values including size of clothes, category and grade to a variable
            clothes_list.append(clothes_final)  # adds clothes_final values to the list clothes_list
    else:  # if num cannot be converted to an integer return error message
        print("Invalid input")
        pass  # loop continues to the next step


def repeat_sorter():
    while True:
        mode = input(
            "do you want manual(m) or automatic(a) mode or are you done(d): ")  # input for the mode option either manual mode, automatic mode or exiting and ending the program
        if mode.lower() == "m":  # checks if the mode is manual (keyword it is looking for is m). .lower() makes it so that it is not case sensitive
            jacket_sorter_manual()
        elif mode.lower() == "a":  # else if the mode input is "a" or "A"
            jacket_sorter_auto()
        elif mode.lower() == "d":  # if mode input = "d" or "D"
            print("clothes sorter shutting down...")
            print("-------------------------------")
            break

        else:  # else if the mode input is none of the above return an error message
            print("Input is invalid. Please input a valid option")
            print("-------------------------------")

    print("All the sorted clothes in your session: \n" + str(clothes_list))


def main():
    repeat_sorter()


if __name__ == "__main__":
    main()
