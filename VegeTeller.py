
def searchIndexByName(source, ingredient):
    start = 0
    end = len(source)

    while start < end:
        mid = (start + end)//2
        if source[mid] == ingredient.lower():
            return mid
        if source[mid] > ingredient.lower():
            end = mid - 1
        else:
            start = mid + 1