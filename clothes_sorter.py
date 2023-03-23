import random
import time

clothes_list = []  # placeholder/empty list for later use

class Sorter():  # create a class called "Sorter"
    def __init__(self):  # initialise class
        pass

    def category(self, size):  # function for categorising clothes
        match size:
            case _ if size < 5:  # rejected
                category = "rejected"
            case _ if 5 <= size <= 10:  # small
                category = "small"
            case _ if 10 < size <= 20:  # medium
                category = "medium"
            case _:  # large
                category = "large"

        return category  # returns category of clothes
    def clothes_sorter_manual(self):  # clothes_sorter function
        while True:
            size = input("input the size of the clothes into the system: ")  # ask for size input for clothes
            if size.isdigit():  # checks if the input can be converted to integer
                size = int(size)
                print(f"category: {self.category(size)} \n {'-' * 50}")  # prints category of clothes
                clothes_final = (str(size) + " inches", self.category(size))
                clothes_list.append(clothes_final)  # adds clothes_final values to the list clothes_list

            else:  # returns a message for invalid input of size
                print("This is not a valid size")
                continue  # skips to the next iteration of the loop

            proceed = input("do you want to continue y/n: ")  # asks if the user wants to continue manual input

            if proceed.lower() == "y":
                pass  # continue to the next step of the loop
            elif proceed.lower() == "n":
                break  # stop the current loop
            else:  # else if the input is invalid, automatically stop the loop
                print("Invalid input. Auto stopping manual input...")
                break

    def clothes_sorter_auto(self):
        num = input("How many clothes would you like to sort: ")  # retrives input for number of clothes you want to input
        if num.isdigit():  # checks if "num" can be converted to an integer
            for i in range(int(num)):  # loop "num" amount of times
                size_auto = random.randint(0, 30)  # generate a random clothes size between 0 and 30
                print(f"Weight of clothes: {size_auto} inches")
                print(f"category: {self.category(size_auto)} \n {'-' * 50}")  # prints category of clothes
                clothes_final = (str(size_auto) + " inches", self.category(size_auto))
                clothes_list.append(clothes_final)  # adds clothes_final values to the list clothes_list
                time.sleep(1)  # delay for 1 second
        else:  # if num cannot be converted to an integer return error message
            print("Invalid input")
            pass  # loop continues to the next step











def repeat_sorter():
    sorter = Sorter()
    while True:
        mode = input("do you want manual(m) or automatic(a) mode or are you done(d): ")
        match mode:
            case "m":
                sorter.clothes_sorter_manual()  # run manual sorter function
            case "a":
                sorter.clothes_sorter_auto()  # run auto sorter function
            case "d":
                print(f"clothes sorter shutting down... \n {'-' * 50}")
                break  # stop the loop
            case _:  # else if the mode input is none of the above return an error message
                print(f"Input is invalid. Please input a valid option \n {'-' * 50}")

    if len(clothes_list) == 0:
        print("Why did you even turn on the sorter?")

    return print(f"All the sorted clothes in your session: \n {str(clothes_list)}")


def main():  # main
    repeat_sorter()


if __name__ == "__main__":
    main()
