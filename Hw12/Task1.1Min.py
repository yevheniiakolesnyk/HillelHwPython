def min_own(*args, list_own=[]):
    list_own.append(args)

    def feature():
        v_min = float('inf')
        for el in list_own[0]:
            if el < v_min:
                v_min = el
        return v_min

    result = feature()
    return result


print(min_own(4, 8, 9, 1, 12, 88, 17, 77))

def logger(func):
    def wrapper():
        result = func.__name__
        return result

    return wrapper()


print(logger(min_own))