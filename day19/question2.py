import re
# Is the Phone Number Formatted Correctly?
# Create a function that accepts a string and returns True if it's in the
# format of a proper phone number and False if it's not. Assume any number
# between 0-9 (in the appropriate spots) will produce a valid phone number.
# medium


def check_num_format(string):
    pattern = r"\([1][2][3]\)\s[0-9]{3}\-[0-9]{4}"
    if re.search(pattern, string):
        print("True")
    else:
        print("False")


# check_num_format("(123) 456-7890")
# check_num_format("1111)555 2345")
check_num_format("098) 123 4567")
