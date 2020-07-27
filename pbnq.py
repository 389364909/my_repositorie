a = 0
b = 1
s = []
for x in range(20):
    a,b = b,a+b
    s.append(a)
print(s)
