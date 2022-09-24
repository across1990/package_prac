
def sort_case(text):
    

    x = list(text.replace(" ", ""))


    upper = []
    lower = []

    for char in x:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char) 
            
    return upper, lower
        