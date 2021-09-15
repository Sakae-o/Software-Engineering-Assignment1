keywords = ["auto",	"break", "case", "char", "const", "continue", "default", "do",
            "double", "else", "enum", "extern",	"float", "for",	"goto",	"if",
            "int",	"long",	"register",	"return", "short", "signed", "sizeof", "static",
            "struct", "switch",	"typedef", "union",	"unsigned",	"void",	"volatile",	"while"]

num = [0 for i in range(32)]


def statistics(words):
    ''' Count the number of each keyword in the text. '''
    for i in range(32):
        num[i] = words.count(keywords[i])


def compute_num(words):
    ''' Compute the total number of the keywords '''
    statistics(words)
    result = 0
    for i in num:
        result += i
    return result
