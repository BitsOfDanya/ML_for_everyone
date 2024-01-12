n, k = map(int, input().split())
ci = sorted(zip(map(int, input().split()), range(n)), key = lambda c: c[0]) # сопоставляем каждому кубику номер, а потом сортируем по цветам
cc = [(0, 0)]
cR = cL = ci[0]
for i in range(1, n):
    if ci[i][0] != cL[0]:
        cc.append((cL[1], cR[1]))
        cL = ci[i]
    cR = ci[i]
cc.append((cL[1], cR[1])) # получили список левого и правого кубиков для каждого цвета
sl = sr = 0
for i in range(len(cc) - 1, 0, -1):
    r = cc[i][1] - cc[i][0]
    nl = min(abs(cc[i][0] - cc[i - 1][1]) + sl, abs(cc[i][1] - cc[i - 1][1]) + sr)
    nr = min(abs(cc[i][0] - cc[i - 1][0]) + sl, abs(cc[i][1] - cc[i - 1][0]) + sr)
    sl, sr = nl + r, nr + r
print(min(sl, sr))
