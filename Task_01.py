# 1. Напишите программу вычисления арифметического выражения
#    заданной строки. Используйте операции +,-,/,* приоритет
#    операций стандартный. 
#    * Добавте скобки, приоритет операций меняется.
# in  2 - 2 + 7 * 3           out  >>  14
# in  2 - (2 + 7) * 2         out  >> -16
# in  101 / 2 - (12 + 8) * 3  out  >> -9.5

actions = {
"^": lambda x, y: str(float(x) ** float(y)),
"*": lambda x, y: str(float(x) * float(y)),
"/": lambda x, y: str(float(x) / float(y)),
"+": lambda x, y: str(float(x) + float(y)),
"-": lambda x, y: str(float(x) - float(y))
}

res = "( 10 + 5 ) * 3 - 8 / 2"

def scob(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] ==  '(':
            n = line. index(")", i)
            lst.append(line[i + 1:n])
            i = n
        else:
            lst.append(line[i])
        i += 1
    return lst

#print(scob(res.split()))  

def in_scob(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            a, b, c = scob(lst[i])
            lst[i] = actions[b](a, c)
    return lst        

#print(in_scob(scob(res.split())))

def result(lst):
    priar = [i for i, j in enumerate(lst) if j in "* /"]
    while priar:
        t = priar[0]
        a, b, c = lst[t - 1: t + 2]
        lst.insert(t - 1, actions[b](a, c))
        del lst[t: t + 3]
        priar = [i for i, j in enumerate(lst) if j in "* /"]
    h = 0
    while len(lst) > 1:
        a, b ,c = lst[: 3]
        del lst[:3]
        lst.insert(0, actions[b](a, c))

    return lst

s2 = "2 - ( 2 + 7 ) * 2"
s3 = "101 / 2 - ( 12 + 8 ) * 3"
print(scob(s2.split()))
print(result(in_scob(scob(s2.split()))))    
print(scob(s3.split()))
print(result(in_scob(scob(s3.split()))))
print(scob(res.split()))
print(result(in_scob(scob(res.split()))))