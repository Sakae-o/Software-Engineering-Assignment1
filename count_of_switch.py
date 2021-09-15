from keywords_num import num



def count(words):
    '''
    Output the number of switch structure
    and the number of "case" each switch structure has.
    '''
    print("switch num:", num[25])

    print("case num:", end=" ")
    case_num = 0
    for i in range(words.index("switch") + 1, words.__len__()):
        if (words[i] == "switch" or i == words.__len__() - 1):
            print(case_num, end=" ")
            case_num = 0
        elif (words[i] == "case"):
            case_num += 1