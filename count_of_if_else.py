from collections import deque



def count_if_else(words):
    ''' Count the number of if-else structure. '''
    stack = deque()
    result = 0

    for i in range(
            words.__len__()):
        if (words[i] == "if" and words[i-1] != "else"):
            stack.append(1)
        if (stack.__len__() != 0):
            if (words[i] == "else" and words[i+1] != "if"):
                if (stack[-1] == 1):
                    result += 1
                    stack.pop()
                elif (stack[-1] == 2):
                    stack.pop()
                    stack.pop()
            elif (words[i] == "else" and words[i+1] == "if" and stack[-1] == 1):
                stack.append(2)
    return result


def count_else(words):
    '''
    Count the number of ending "else" in each
    if-else structure and if-elseif-else structure.
    '''
    result = 0
    for i in range(words.__len__()):
        if ((words[i] == "else" and words[i+1] != "if")):
            result += 1
    return result
