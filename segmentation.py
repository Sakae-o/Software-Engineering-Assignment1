import os



def segment(root):
    '''
    Break each row of the text into a list of individual words
    without '(', ')', ';', ';', '{' and '}',
    then merge those lists into one list which will be returned.
    '''
    f = open(root, "r")
    lines = f.readlines()
    result = []
    for line in lines:
        line = line.translate({ord(i): " " for i in "();:{}"})
        line_split = line.split()
        result.extend(line_split)
    return result
