string1 = "This is a string."
string2 = " This is another string."
string3 = string1.upper() + string2
print(string3)

d = "qwerty"
ch = d[1:5:2]
print(ch)

x = 3
y = 5
z = 5 ** 3
print(z)

param = "string" + str(15)
print(param)

n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", "{:5.2f}".format(n3))

a = 1 / 3
print("{:7.3f}".format(a))

a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
help(list1.remove)
list1[0] = 76
list1.append(22)
list1.insert(7, 1)
list1.pop(3)
list1.pop(len(list1) - 1)
print(list1)

list1.sort(reverse=True)
print(list1)
list2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2)
print(lis)

print(dir(tuple))
help(tuple.index)
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq.count(8))
print(seq.index(44))
listSeq = list(seq)
print(type(listSeq))
listSeq.sort()
listSeq.append(77)
print(listSeq)

D = {"food": "Apple", "quantity": 4, "color": "Red"}
print(D["food"])
D["quantity"] += 10
print(D["quantity"])

dp = {"name": input(), "age": input()}
print(dp)

rec = {"name": {"firstname": "Bob", "lastname": "Smith"},
       "job": ["dev", "mgr"],
       "age": 25}
print(rec["name"])
print(rec["name"]["firstname"])
print(rec["job"])
rec["job"].append("janitor")
print(rec)
