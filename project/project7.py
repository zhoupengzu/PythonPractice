# 将一个字符串中的每个单词首字母大写


def capitalize(string):
    string = string.capitalize()
    isEmpty = False
    result = ""
    for c in string:
        if c == " ":
            isEmpty = True
            result += c
        else:
            if c.isalpha() and isEmpty:
                result += c.capitalize()
            else:
                result += c
            isEmpty = False
    return result


print(capitalize("1 w 2 r 3g"))
