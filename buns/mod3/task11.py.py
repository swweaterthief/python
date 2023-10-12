a = [[]]
s = input()
for i in s:
    if i != ' ':
        a[0].append(i)
k = len(a[0])

for i in range(k - 1):
    s = input()
    a.append([])
    for j in s:
        if j != ' ':
            a[i + 1].append(j)

ans = 'Ничья'
for i in range(k):
    t = a[i][0]
    if a[i].count(t) == 3 and t != '_':
        ans = t

for i in range(k):
    t = a[i][0]
    flag = True
    for j in range(k):
        if t != a[j][i]:
            flag = False
    if flag and t != '_':
        ans = t

flag = True
t = a[0][0]
for i in range(k):
    if a[i][i] != t:
        flag = False
if flag and t != '_':
    ans = t

flag = True
t = a[0][-1]
for i in range(k):
    if a[i][-i - 1] != t:
        flag = False
if flag and t != '_':
    ans = t

print(ans)
