
def main():

    def first_recurring(given_string):

        return[char for char in given_string if given_string.count(char) > 1][0]

    print(first_recurring("DBCABA"))


if __name__ == "__main__":
    main()
