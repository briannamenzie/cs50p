def main():
    # Prompt user for time
    time = input("What time is it? ")
    # call convert function to convert time to float and store in variable converted
    converted = convert(time)
    # check if converted time is between 7 and 8, 12 and 13, or 18 and 19 and print corresponding meal time
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")
    # if converted time does not fall within any of the specified ranges, do nothing (pass)
    else:
        pass


# this function takes a time in the format "H:M" and converts it to a float representing the time in hours
def convert(time):
    # split the input time into hours and minutes using the split method and store in variables h and m
    h, m = time.split(":")
    # convert hours to float and add minutes converted to hours (by dividing by 60) and return the result
    return float(h) + float(m) / 60

# call the main function, which starts the program
if __name__ == "__main__":
    main()