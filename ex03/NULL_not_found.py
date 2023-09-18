def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f"Nothing: {object} {type(object)}")
        elif isinstance(object, float) and str(object) == "nan":
            print(f"Cheese: nan {type(object)}")
        elif isinstance(object, bool) and object is False:
            print(f"Fake: {object} {type(object)}")
        elif isinstance(object, int) and object == 0:
            print(f"Zero: {object} {type(object)}")
        elif isinstance(object, str) and object == '':
            print(f"Empty: {type(object)}")
        else:
            print("Type not Found")
            return 1
        return 0
    except:
        print("Error occurred")
        return 1
