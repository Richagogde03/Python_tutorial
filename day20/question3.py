# Spelling Bee
# medium

def validate_spelling(string1):
    char_to_ignore = [".", "!", "?"]
    new_string = ""
    for i in string1:
        if i in char_to_ignore:
            continue
        else:
            new_string += i
    splitting = new_string.split(" ")
    chars = [char for char in splitting if len(char) == 1]

    word = splitting[-1].upper()

    for i in word:
        if i not in chars:
            return False

    return True


print(validate_spelling("C. Y. T. O. P. L. A. S. M. Cytoplasm?"))
print(validate_spelling("P. H. A. R. A. O. H. Pharaoh!"))
print(validate_spelling("H. A. N. K. E. R. C. H. E. I. F. Handkerchief."))
print(validate_spelling("P. A. R. L. I. A. E. P. N. T. Parliament!"))
print(validate_spelling("E. M. B. A. R. R. A. S. S. Embarrass!"))
