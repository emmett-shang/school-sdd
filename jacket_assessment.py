import random

import time

clothes_list = []  # list to collect sorted clothes


def size_category(category, grade):
    if category == "rejected":
        graded = "N/A"
        return graded
    else:
        grade_map = {"j": "junior", "s":"senior"}

    return category, grade_map[grade]


def jacket_sorter_manual():  # clothes_sorter function

    while True:
        size = input("input the size of the jacket into the system: ")  # ask for size input for clothes
        if size.isdigit():  # checks if the input can be converted to integer
            size = int(size)
            grade = input("Junior(j) or Senior(s)? ")  # ask for the grade of clothes, whether its junior or senior
            if grade.lower() == "j" or grade.lower() == "s":  # checks for valid input
                match size:
                    case _ if size < 5:
                        category = "rejected"
                    case _ if 5 <= size <= 10:
                        category = "small"
                    case _ if 10 < size <= 20:
                        category = "medium"
                    case _ if size > 20:
                        category = "large"

                print(f"size and grade: {str(size_category(category, grade))} \n {'-' * 50}")
                clothes_final = (size, *size_category(category, grade))
                clothes_list.append(clothes_final)

            else:  # returns a message for invalid input of grade
                print("This is not a valid grade")
                continue  # skips to the next iteration of the loop
        else:  # returns a message for invalid input of size
            print("This is not a valid size")
            continue

        proceed = input("do you want to continue y/n: ")  # asks if the user wants to continue manual input
        if proceed.lower() == "y":
            pass  # continue to the next step of the loop
        elif proceed.lower() == "n":
            break  # stop the current loop
        else:  # else if the input is invalid, automatically stop the loop
            print("Invalid input. Auto stopping manual input...")
            break


def size_category_auto(category):
    grade = ""
    match category:
        case "rejected":
            grade = "N/A"
        case "small":
            if random.random() <= 0.75:  # returns a random value between 0 and 1. If the value is below 0.75 grade = Junior making it a 75% chance
                grade = "junior"
            else:  # else returns senior grade
                grade = "senior"
        case "medium":
            if random.random() <= 0.5:  # if the value is below 0.5, grade = junior (50% chance)
                grade = "junior"
            else:  # else grade = senior
                grade = "senior"
        case "large":
            if random.random() <= 0.25:  # if the value is below 0.25, grade = junior (25% chance)
                grade = "junior"
            else:  # else grade = senior
                grade = "senior"

    return category, grade


def jacket_sorter_auto():
    num = input("How many clothes would you like to sort: ")  # retrives input for number of clothes you want to input
    if num.isdigit():  # checks if "num" can be converted to an integer
        for i in range(int(num)):  # loop "num" amount of times
            size_auto = random.randint(0, 30)  # generate a random clothes size between 0 and 30

            match size_auto:
                case _ if size_auto < 5:
                    category = "rejected"
                case _ if 5 <= size_auto <= 10:
                    category = "small"
                case _ if 10 < size_auto <= 20:  # medium
                    category = "medium"
                case _ if size_auto > 20:  # large
                    category = "large"

            print(f"Weight of clothes: {size_auto} \n size and grade: {str(size_category_auto(category))} \n {'-' * 50}")
            time.sleep(1)  # delay for 1 second
            clothes_final = (size_auto, *size_category_auto(category))
            clothes_list.append(clothes_final)

    else:  # if num cannot be converted to an integer return error message
        print("Invalid input")
        pass  # loop continues to the next step


def repeat_sorter():
    while True:
        mode = input(
            "do you want manual(m) or automatic(a) mode or are you done(d): ")  # input for the mode option either manual mode, automatic mode or exiting and ending the program
        match mode.lower():
            case "m":
                jacket_sorter_manual()  # runs manual mode
            case "a":
                jacket_sorter_auto()  # runs auto mode
            case "d":
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
