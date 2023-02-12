def student(name):
    lst_names = []
    def inner():
        lst_names.append(name)
        return lst_names

    return inner

std_1 = student('Denis')()
std_2 = student('Olga')()
std_3 = student('Max')()


print(std_1)
print(std_2)
print(std_3)
