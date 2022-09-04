def Default():
    return '\033[0m'

def Bold(str):
    return '\033[1m' + str + Default()

def Underline(str):
    return '\033[1;4m' + str + Default()