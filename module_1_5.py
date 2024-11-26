immutable_var = "кортеж",1,3,True
print("Immutable tuple:", immutable_var)
#immutable_var[2] = 2
#print(immutable_var) при выполнении возникает ошибка, т.к.попытка изменить элемент кортежа некорректна
mutable_list = ["список",1,2,'a']
mutable_list[0] = "Modified"
print("mutable list:",mutable_list)