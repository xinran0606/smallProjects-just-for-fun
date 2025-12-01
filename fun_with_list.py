def a_words_to_number():
    """The program reads a comma-separated list of number words (zero to nine)
    and converts them to a list of digits."""

    valid_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    while True:
        x = input("Please give the sequence of words from zero to nine (comma separated): ").lower()
        lst = x.split(",")

        try:
            string_num = ""
            for i in lst:
                string_num += str(valid_words[i])
            number = int(string_num)
            return number

        except KeyError:
            print("Invalid input. Please only use words zero-nine.")


def b_number_insert_list():
    """The program reads in a number from the console and insert it into the list a such that the sorting of a is maintained."""
    a = [2, 4, 6, 8, 10, 12, 14, 16]
    print("Here is list a: ", a)

    while True:
        x = input("Please give an integer: ")
        try:
            num = int(x)
            break
        except ValueError:
            print("Invalid input, please gibe an integer: ")

    # a.append(num)
    # a.sort()

    insert_index = 0
    for i in a:
        if i < num:
            insert_index += 1
        else:
            break

    a.insert(insert_index, num)
    print("The new element is at the index: \n", insert_index)
    print("Updated list: ")
    return a

def c_find_number_tuple():
    """The program reads in a number from the console and searches for a matching tuple based on the first entry."""
    c = [(35, 59), (75, 60), (48, 25), (21, 4), (2, 100), (31, 6)]
    print("Here is a list of tuples: ", c)

    while True:
        x = input("Please give an integer: ")
        try:
            num = int(x)
            break
        except ValueError:
            print("Invalid input, please give an integer: ")

    for i in c:
        if i[0] == num:
            print("Yes you found the tuple, and the second entry is: ")
            return i[1]

    print("No tuple found with first entry, do you want to try again?")
    x = input("Yes or click on any one to quit:").lower()
    if x == "yes":
        c_find_number_tuple()
    else:
        print("Thanks for using.")
        quit()

print(a_words_to_number())
print(b_number_insert_list())
print(c_find_number_tuple())