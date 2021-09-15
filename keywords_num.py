keywords = ["auto",	"break", "case", "char", "const", "continue", "default", "do",
            "double", "else", "enum", "extern",	"float", "for",	"goto",	"if",
            "int",	"long",	"register",	"return", "short", "signed", "sizeof", "static",
            "struct", "switch",	"typedef", "union",	"unsigned",	"void",	"volatile",	"while"]

num = [0 for i in range(32)]


def statistics(lines):
    ''' Count the number of each keyword in the text. '''
    for line in lines:
        line = line.translate({ord(i): " " for i in "();:{}"})
        line_split = line.split()
        print(line_split)
        for i in range(32):
            num[i] += line_split.count(keywords[i])


def compute_num(lines):
    ''' Compute the total number of the keywords '''
    statistics(lines)
    result = 0
    for i in num:
        result += i
    print("\narray num:", num)
    return result