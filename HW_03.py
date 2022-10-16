# 3. Написать функцию, аргументы имена сотрудников,
#    возвращает словарь, ключи — первые буквы имён,
#    значения — списки, содержащие имена,
#    начинающиеся с соответствующей буквы.
# in "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']} 

def sort_list(*args):
    name = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in name:
            name[letter] = [i]
        name[letter] += [i]

    return name


print(sort_list("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))