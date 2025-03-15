def find_peek(list):
    result = []
    if len(list)>1:
        for index, value in enumerate(list):
            result.append(value-list[index-1])
        return result.index(max(result))
    elif len(list)==1:
        return 0
    else:
        return -1
