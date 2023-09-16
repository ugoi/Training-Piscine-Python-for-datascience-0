ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello" : "titi!"}

#your code here
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