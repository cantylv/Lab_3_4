def print_result(test):
    def wrapper(*args):
        print(test.__name__)
        test(*args)
        arr = test(*args)
        if type(arr) == list:
            for iter in arr:
                print(iter)
        elif type(arr) == dict:
            for iter in arr.keys():
                print(f"{iter} = {arr[iter]}")
        else:
            print(test())
        return arr
    return wrapper