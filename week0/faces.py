# this function converts :) to 🙂 and :( to 🙁
def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

# main function to get user input and print the converted text
# controls the program flow calls the convert function
def main():
    text = input("Input? ")
    print(convert(text))

# call the main function, which starts the program
main()