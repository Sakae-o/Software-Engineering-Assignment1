import os



def segment(root):
    '''
    Break each row of the text into a list of individual words
    without ' ', '(', ')', ':' , and ',',
    then merge those lists into one list which will be returned.
    '''
    f = open(root, "r")
    lines = f.readlines()
    result = []
    is_annotation = 0
    for line in lines:
        # Replace some words with special marks. #
        # Then split the words in the line into a list. #
        line = line.translate({ord(i): " " for i in "():,"})
        line = line.translate({ord("\""): " @ "})
        line = line.translate({ord("/"): " $ "})
        line = line.translate({ord("*"): " * "})
        line = line.translate({ord(";"): " ; "})
        line = line.translate({ord("{"): " { "})
        line = line.translate({ord("}"): " }"})
        line_split = line.split()

        line_split = delete_annotation_1(line_split)
        line_split = delete_strings(line_split)
        result.extend(line_split)

    result = delete_annotation_2(result)
    return result


def delete_strings(list):
    '''
    Delete the two quotation marks, which has been replaced
    with "@",  and delete all the words between them.
    '''
    if (list.count("@") <= 1):
        return list
    flag = 0
    new_list = []
    for i in list:
        if (flag == 0):
            if (i == "@"):
                flag = 1
            else:
                new_list.append(i)
        elif (flag == 1):
            if (i == "@"):
                flag = 0
    return new_list


def delete_annotation_1(list):
    '''
    Delete the mark "//" , which has been replaced with double "$",
    and delete all the words after it in a row.
    '''
    for i in range( list.__len__() - 1):
        if (list[i] == "$" and list[i+1] == "$"):
            return list[:i]
    return list


def delete_annotation_2(list):
    '''
    Delete each set of the marks "/*" and "*/", which has been
    replaced with "$*" and "*$", and delete all the words between them in each set.
    '''
    flag = 0
    result = []

    i = 0
    while (i < list.__len__()):
        if (flag == 0):
            if (list[i] == "$" and list[i+1] == "*"):
                flag = 1
                i += 1
            else:
                result.append(list[i])
        elif (flag == 1):
            if (list[i] == "*" and list[i+1] == "$"):
                flag = 0
                i += 1
        i += 1

    return result
