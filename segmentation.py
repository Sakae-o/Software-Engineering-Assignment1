import os



def segment(root):
    '''
    Break each row of the text into a list of individual words
    without ' ', '(', ')', ':' , ',' and ';',
    then merge those lists into one list which will be returned.
    '''
    f = open(root, "r")
    lines = f.readlines()
    result = []
    is_annotation = 0
    for line in lines:
        line = line.translate({ord(i): " " for i in "();:,"})
        line = line.translate({ord("\""): " @ "})
        line = line.translate({ord("/"): " $ "})
        line_split = line.split()

        if (is_annotation == 0):
            line_split = delete_annotation(line_split)
            line_split = delete_strings(line_split)
            is_annotation = is_annotation_start(line_split)
            result.extend(line_split)
        elif (is_annotation == 1):
            if (is_annotation_end(line_split) == 1):
                is_annotation = 0
                result.extend(line_split)

    return result


def delete_strings(list):
    ''' Delete the tow quotation marks and all the words between them. '''
    if (list.count("@") == 0 or list.count("@") == 1):
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


def delete_annotation(list):
    ''' Delete the mark "//" and all the words after it in a row. '''
    for i in range( list.__len__() - 1):
        if (list[i] == "$" and list[i+1] == "$"):
            return list[:i]
    return list


def is_annotation_start(line):
    '''
    Judge whether the start flag of annotation exists in this row.
    Incidentally delete the flag and all the words after it.
    '''
    if (line.count("$") == 0):
        return 0
    for i in range(line.__len__() - 1):
        if (line[i] == "$" and line[i+1] == "*"):
           del line[i:]
           return 1
    return 0


def is_annotation_end(line):
    '''
    Judge whether the end flag of annotation exists in this row.
    Incidentally delete the flag and all the words before it.
    '''
    if (line.count("$") == 0):
        return 0
    for i in range(line.__len__() - 1):
        if (line[i] == "*" and line[i+1] == "$"):
            del line[:i+2]
            return 1
    return 0
