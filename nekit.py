import random

t = []
for _ in range(100):
    x = 0
    for _ in range(90):
        if random.random() > 0.29:
            x += 1
    t.append(x)

t.sort()
print(t[0], t[-1])
print(t)

e1 = []
e2 = []
e3 = []
j = 0
fx = 0

for i in t:
    if j == i:
        continue
    fx += t.count(i)
    e1.append(i)
    e2.append(str(fx / 100).replace('.', ','))
    e3.append(str(t.count(i) / 100).replace('.', ','))
    j = i

print(e1)
print(e2)
print(e3)

e4 = [[], [], [], [], [], [], [], [], [], []]
for i in t:
    for k in range(1, 11):
        if i < t[0] + 2 * k:
            e4[k - 1].append(i)
            break
print(e4)

g = []
for i in e4:
    g.append(len(i))
    print(len(i), end=' ')
