size = int(input())
a = []
ans = []
for i in range(size):
    a.append(list(range(1, size + 1)))

for i in range(size):
    t = []
    for j in range(size):
        t.append(a[j][i])
    ans.append(t)

for i in a:
    print(*i, sep=', ')
print()
for i in ans:
    print(*i, sep=', ')
