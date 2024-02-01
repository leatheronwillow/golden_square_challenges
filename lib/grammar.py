def grammar(text):

    if text == "":
        return "text is empty"
    
    statement = "first letter is "

    if text[0].isupper():
        statement += "capital "
    else:
        statement += "not capital "
    
    punctuation = "!?."

    if text[-1] in punctuation:
        statement += "and punctuation is correct"
    else:
        statement += "but punctuation is incorrect"

    return statement