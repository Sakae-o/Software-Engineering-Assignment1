from keywords_num import num



def count(words):
    '''
    Output the number of switch structure
    and the number of "case" each switch structure has.
    '''
    case_list = []

    if (num[25] == 0):
        case_list.append(0)
        return 0, case_list

    case_num = 0
    for i in range(words.index("switch") + 1, words.__len__()):
        if (words[i] == "switch" or i == words.__len__() - 1):
            case_list.append(case_num)
            case_num = 0
        elif (words[i] == "case"):
            case_num += 1
    return num[25], case_list
