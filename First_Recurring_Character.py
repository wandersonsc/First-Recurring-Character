
def main():

    def first_recurring(given_string):

        return[char for char in given_string if given_string.count(char) > 1][0]

    output = first_recurring("DBCABA")
    print(output)

if __name__ == "__main__":
    main()
