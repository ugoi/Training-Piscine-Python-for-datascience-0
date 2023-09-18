def all_thing_is_obj(obj: any) -> int:
    if isinstance(obj, list):
        print(f"List : {type(obj)}")
    elif isinstance(obj, tuple):
        print(f"Tuple : {type(obj)}")
    elif isinstance(obj, set):
        print(f"Set : {type(obj)}")
    elif isinstance(obj, dict):
        print(f"Dict : {type(obj)}")
    elif isinstance(obj, str):
        print(f"Brian is in the kitchen : {type(obj)}")
    else:
        print("Type not found")
    return 42
