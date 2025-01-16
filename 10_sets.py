#set significa grupo o conjunto no se pueden repetir elemento y no se pueden ornear
primer = {1, 1, 2, 2, 3, 4,6,7,8,9}
#print(primer)
primer.add(5)
print(primer)
#primer.remove(2)
#print(primer)
#creamos un set en base a nuna lista
segundo = [1,2,3,4,5,8]
segundo = set(segundo)

print(segundo)
#print(primer|segundo) #une los elemento entre el primer elemnto
#print(primer&segundo)
#print(primer-segundo)
print(primer^segundo)

#buscar un elemnto
if 512 in segundo:
    print("si esta")
else:
    print("no esta")
