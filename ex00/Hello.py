"""
This script initializes four basic data structures: a list, a tuple, a set, and a dictionary.
- The list and the tuple both contain greeting messages.
- The set contains different versions of a greeting.
- The dictionary maps a greeting to a response.

The script then:
1. Modifies the second element of the list.
2. Since tuples are immutable, it converts the tuple to a list, modifies it, and converts it back.
3. Removes an item from the set and adds a new one.
4. Modifies the value of a key in the dictionary.

Finally, the script prints all the modified data structures.
"""

def process_data():
    ft_list  = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set   = {"Hello", "tutu!"}
    ft_dict  = {"Hello" : "titi!"}

    ft_list[1] = "World"

    ft_tuple_lst = list(ft_tuple)
    ft_tuple_lst[1] = "Germany"
    ft_tuple = tuple(ft_tuple_lst)

    ft_set.remove("tutu!")
    ft_set.add("Heilbronn")

    ft_dict["Hello"] = "42Heilbronn"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

def main():
    process_data()

if __name__ == "__main__":
    main()
