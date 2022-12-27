def add(x, y):
    return x + y

print(add(1, 2))
print(add(1, "a")) # ERR
add.x = 1 # ERR

def add2(x: int, y: int) -> str: # ERR
    return x + y

print(add2(1, 2))

# ERR
for i in [1, 2, 3]:
    j = i + "aa"
    print(j)

i: int # OK
i = 1
i: str # ERR
i = "aa" if True else "bb"
i: str # OK

while "aaa": # ERR
    i += 1 # ERR
    break

class C:
    x = 1 + "a" # ERR

dic = {"a": 1, "b": 2}
print(dic["c"]) # ERR

a = [1, 2, 3]
print(a[4]) # ERR
