import random

import time

clothes_list = []  # list to collect sorted clothes


class Sorter:  # create a class called "Sorter"
    def __init__(self):  # initialise class
        pass

    def grade_category(self, category, grade):  # function for sorting grade
        if category == "rejected":
            grade_map = {"j": "N/A", "s": "N/A"}  # maps keyword "j" and "s" to "N/A"
        else:
            grade_map = {"j": "junior", "s": "senior"}  # maps keyword "j " and "s" to "junior" and "senior"

        return category, grade_map[grade]  # returns the parameter "category" and mapped keyword to "grade" in grade_map

    def jacket_sorter_manual(self):  # clothes_sorter_manual function

        while True:
            size = input("input the size of the jacket into the system: ")  # ask for size input for clothes
            if size.isdigit():  # checks if the input can be converted to integer
                size = int(size)
                grade = input("Junior(j) or Senior(s)? ")  # ask for the grade of clothes
                if grade.lower() == "j" or grade.lower() == "s":  # checks for valid grade input
                    match size:
                        case _ if size < 4:  # rejected
                            category = "rejected"
                        case _ if 4 <= size <= 10:  # small
                            category = "small"
                        case _ if 9 < size <= 20:  # medium
                            category = "medium"
                        case _ if size > 19:  # k large
                            category = "large"

                    print(f"category and grade: {str(self.grade_category(category, grade))} \n {'-' * 49}")  #print category and grade
                    clothes_final = (str(size) + " inches", *self.grade_category(category, grade))
                    clothes_list.append(clothes_final)  # adds clothes_final value to clothes_list
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
                break  # stop manual mode
            else:  # else if the input is invalid, automatically stop manual mode
                print("Invalid input. Auto stopping manual input...")
                break

    def grade_category_auto(self, category):  # function for sorting grade for auto mode
        grade = ""
        match category:
            case "rejected":
                grade = "N/A"
            case "small":
                if random.random() <= 0.75:  # returns a random value between 0 and 1. If the value is below 0.75 grade = Junior making it a 75% chance
                    grade = "junior"
                else:
                    grade = "senior"
            case "medium":
                if random.random() <= 0.5:  # junior = 50%
                    grade = "junior"
                else:
                    grade = "senior"
            case "large":
                if random.random() <= 0.25:  # junior = 25 %
                    grade = "junior"
                else:
                    grade = "senior"

        return category, grade  #returns parameter category and grade

    def jacket_sorter_auto(self):
        num = input(
            "How many clothes would you like to sort: ")  # retrives input for number of clothes you want to input
        if num.isdigit():  # checks if "num" can be converted to an integer
            for i in range(int(num)):  # loop "num" amount of times
                size_auto = random.randint(0, 30)  # generate a random clothes size between 0 and 30
                match size_auto:
                    case _ if size_auto < 5:  # rejected
                        category = "rejected"
                    case _ if 5 <= size_auto <= 10:  # small
                        category = "small"
                    case _ if 10 < size_auto <= 20:  # medium
                        category = "medium"
                    case _ if size_auto > 20:  # large
                        category = "large"

                print(f"Size of clothes: {size_auto} inches \n size and grade: {str(self.grade_category_auto(category))} \n {'-' * 50}")  # prints size of clothes and grade
                time.sleep(1)  # delay for 1 second
                clothes_final = (str(size_auto) + " inches", *self.grade_category_auto(category))
                clothes_list.append(clothes_final)  # adds clothes_final value to clothes_list
        else:  # if num cannot be converted to integer
            print("Invalid input")
            pass  # loop continues to the next step


def repeat_sorter():
    sorter = Sorter()
    while True:
        mode = input(
            "do you want manual(m) or automatic(a) mode or are you done(d): ")  # input for the mode option either manual mode, automatic mode or exiting and ending the program
        match mode.lower():
            case "m":
                sorter.jacket_sorter_manual()  # run manual sorter function
            case "a":
                sorter.jacket_sorter_auto()  # runs auto sorter function
            case "d":
                print(f"clothes sorter shutting down... \n {'-' * 50}")
                break  # end while loop
            case _:  # else if the mode input is none of the above return an error message
                print(f"Input is invalid. Please input a valid option \n {'-' * 50}")

    if len(clothes_list) == 0:
        print("Why did you even turn on the sorter?")

    print("All the sorted clothes in your session: \n" + str(clothes_list))  # prints all sorted clothes


def main():  # main
    repeat_sorter()


if __name__ == "__main__":
    main()  #run main function
