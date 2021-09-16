from collections import deque



def count(words):
    ''' Count the number of if-else structure. '''
    stack = deque()
    result = 0

    for i in range(words.index("if"), words.__len__()):
        if (words[i] == "if" and words[i-1] != "else"):
            stack.append(1)
        if (stack.__len__() != 0):
            if (words[i] == "else{" or words[i] == "else{}" or (words[i] == "else" and words[i+1] != "if")):
                stack.pop()
                result += 1
            elif (words[i] == "else" and words[i+1] == "if"):
                stack.pop()
    return result
