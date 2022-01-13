def double_char(phrase):
    new_phrase = ""
    for char in phrase:  # "S"
        # '' <- "SS"
        # 'SS' <- "tt"
        # 'SStt' <- 'rr'
        new_phrase += char * 2
        # new_phrase += char
    return new_phrase


print(double_char("String"))  # ➞ "SSttrriinngg"
print(double_char("Hello World!"))  # ➞ "HHeelllloo  WWoorrlldd!!"
print(double_char("1234!_ "))  # ➞ "11223344!!__  "
