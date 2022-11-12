def field(list, *args):
    if len(args) == 0:
        print("Введите, пожалуйста, название (-я) поля (-ей) через пробел:")
        fields = input()
        args = fields.split()
    elif len(args) == 1:
        value_fields = []
        for iter in list:
            for key,word in iter.items():
                if key==args[0]:
                    value_fields.append(word)
        print(value_fields)
    else:
        arr = []
        for iter in list:
            temp = {}
            for arg in args:
                for key,word in iter.items():
                    if key == arg:
                        temp[key]=word
            if len(temp)!=0:
                arr.append(temp)
        print(arr)
    return 0

