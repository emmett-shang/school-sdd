import random  # import the libary, random

import time  # import the library, time

clothes_list = []  # placeholder/empty list for later use


def clothes_sorter_manual():  # clothes_sorter function
    while True:
        size = input("input the size of the clothes into the system: ")  # ask for size input for clothes
        if size.isdigit():  # checks if the input can be converted to integer
            size = int(size)  # converts size into integer
            match size:
                case _ if size < 5:  # rejected
                    category = "rejected"
                case _ if 5 <= size <= 10:  # small
                    category = "small"
                case _ if 10 < size <= 20:  # medium
                    category = "medium"
                case _:  # large
                    category = "large"
            clothes_final = (str(size) + " inches", category)  # adds all the values including size, category and grade into a variable
            clothes_list.append(clothes_final)  # adds clothes_final values to the list clothes_list
            print(f"category: {category} \n {'-' * 50}")
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


def clothes_sorter_auto():
    num = input("How many clothes would you like to sort: ")  # retrives input for number of clothes you want to input
    if num.isdigit():  # checks if "num" can be converted to an integer
        for i in range(int(num)):  # loop "num" amount of times
            size_auto = random.randint(0, 30)  # generate a random clothes size between 0 and 30
            print(f"Weight of clothes: {size_auto} inches")
            match size_auto:
                case _ if size_auto < 5:  # rejected
                    category = "rejected"
                case _ if 5 <= size_auto <= 10:  # small
                    category = "small"
                case _ if 10 < size_auto <= 20:  # medium
                    category = "medium"
                case _:  # large
                    category = "large"

            print(f"category: {category} \n {'-' * 50}")
            clothes_final = (str(size_auto) + " inches", category)  # assigns or the values including size of clothes, category and grade to a variable
            clothes_list.append(clothes_final)  # adds clothes_final values to the list clothes_list
            time.sleep(1)  # delay for 1 second
    else:  # if num cannot be converted to an integer return error message
        print("Invalid input")
        pass  # loop continues to the next step

    # exit and ending the loop


# prints everything in the list "clothes_list", which returns all the sorted clothes

def repeat_sorter():
    while True:
        mode = input("do you want manual(m) or automatic(a) mode or are you done(d): ")
        match mode:
            case "m":
                clothes_sorter_manual()
            case "a":
                clothes_sorter_auto()
            case "d":  # if mode input = "d" or "D"
                print(f"clothes sorter shutting down... \n {'-' * 50}")
                break
            case _:  # else if the mode input is none of the above return an error message
                print(f"Input is invalid. Please input a valid option \n {'-' * 50}")

    return print(f"All the sorted clothes in your session: \n {str(clothes_list)}")


def main():
    repeat_sorter()


if __name__ == "__main__":
    main()
