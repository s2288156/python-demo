# list
l1 = ["Java", "Python", "C++", "C#"]

print(l1)
l1.append("PHP")
print(l1)

l2 = ["Go", "JS"]

l3 = l1 + l2

print(l3)

print("Go is in l1 :\t\t", "Go" in l1)
print("Go is not in l1 :\t", "Go" not in l1)
print("Go is in l2 :\t\t", "Go" in l2)

# tuple 不可变的list
print("################# ", "tuple 不可变的list")

t1 = ("a", "b")

print(t1)

# dict 相当于Java的map
print("################# ", "dict 相当于Java的map")

d1 = {"a": 1, "b": 2}
print(d1)
print("d1.get(\"b\") : ", d1.get("b"))
print("d1[\"b\"] : ", d1["b"])
print("1 in d1: ", 1 in d1)
print("a in d1: ", "a" in d1)
