1
a, b = map(int, input().split())
u, v = map(int, input().split())

if (a < u and b < v) or (a < v and b < u):
    print(0)
    exit()

if (a // 2 < u and b < v) or (a // 2 < v and b < u):
    print(1)
    exit()
    
if (b // 2 < u and a < v) or (b // 2 < v and a < u):
    print(1)
    exit()
    
print(-1)



2
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(5)
elif n == 3:
    print(21)
elif n == 4:
    print(41)
else:
    summ = 41
    s = 4
    k = 6
    r = (k * 2 - 4) // 2
    for i in range(5, n+1):
        if i % 2 == 1:
            summ += k * 8
            s = s * 2
            k += s
            r = (k * 2 - 4) // 2
        else:
            summ += 4 + r * 4
    print(summ)









3
def decrypt(alice_cipher, step):
    n = len(alice_cipher)
    original = [''] * n
    index = 0
    
    for char in alice_cipher:
        original[index] = char
        index = (index + step) % n
    
    return ''.join(original)

def encrypt(original, step):
    n = len(original)
    cipher = [''] * n
    index = 0
    
    for i in range(n):
        cipher[i] = original[index]
        index = (index + step) % n
    
    return ''.join(cipher)

alice_cipher = input()
original_string = decrypt(alice_cipher, 3)
bob_cipher = encrypt(original_string, 5)
print(bob_cipher)




4
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















5
import heapq

n, s = map(int, input().split())
times = list(map(int, input().split()))

processors = []
heapq.heapify(processors)

min_processors = 0  

for t in times:
    while processors and processors[0] <= t:
        heapq.heappop(processors)

    heapq.heappush(processors, t + s)

    min_processors = max(min_processors, len(processors))

print(min_processors)
