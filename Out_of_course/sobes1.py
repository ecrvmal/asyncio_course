def some_func1 (arr1, arr2):
    result = set(arr2) - set(arr1)
    return result


def some_func2(arr1, arr2):
    result = []
    for i in arr2:
        if i not in arr1:
            result.append(i)
    return result

def some_func3(arr1, arr2):
    result =  list(map( lambda x: x **3    , arr2))
    # result =  list(map( lambda x: filter( x not in arr1 ), arr2))
    result =  list(filter((lambda x: x not in arr1), arr2))
    return result

def some_func4(arr1, arr2):
    for i in arr1:
        if i in arr2:
            arr2.remove(i)
    arr2.sort(reverse=True)
    return arr2


def la(x):
    return x not in arr1


arr1 = [7, 2, 5, 3 , 5, 3]
arr2 = [7, 2, 5, 5, 4, 6, 3, 5, 3]
print(some_func4(arr1, arr2))