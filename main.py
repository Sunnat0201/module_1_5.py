#immutable_var = (1 , "banana" , True, 1.45)
#print(immutable_var)
#immutable_var [1] = apple
#print(immutable_var)
#Значения в кортеже не изменяется, так как кортеж - это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных.
mutable_list = [1, "banana", "apple", "summer", 1.54]
print (mutable_list)
mutable_list[0] = 10
mutable_list[1] = "homework"
print (mutable_list)