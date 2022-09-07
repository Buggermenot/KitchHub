class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def Default():
    return '\033[0m'

def Bold(string):
    return '\033[1m' + str(string) + Default()
2
def Underline(string):
    return '\033[1;4m' + str(string) + Default()

def Color_PURPLE(string):
    return Color.PURPLE + str(string) + Default()

def Color_CYAN(string):
    return Color.CYAN + str(string) + Default()

def Color_DARKCYAN(string):
    return Color.DARKCYAN + str(string) + Default()

def Color_BLUE(string):
    return Color.BLUE + str(string) + Default()

def Color_GREEN(string):
    return Color.GREEN + str(string) + Default()

def Color_YELLOW(string):
    return Color.YELLOW + str(string) + Default()

def Color_RED(string):
    return Color.RED + str(string) + Default()