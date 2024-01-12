n, k = map(int, input().split())
colors = list(map(int, input().split()))
l = [-1 for _ in range(k)]
r = [-1 for _ in range(k)]

for i, val in enumerate(colors):
    if l[val-1] == -1:
        l[val-1] = i
    r[val-1] = i

left = []
right = []

for i in range(len(r)):
    if l[i] != -1:
        left.append(l[i])
    if r[i] != -1:
        right.append(r[i])

time = right[0]
last_finish = right[0]

for i in range(1, len(right) - 1):
    if abs(last_finish - right[i+1]) < abs(last_finish - left[i+1]):
        time += abs(last_finish - right[i])
        last_finish = left[i]
    else:
        time += abs(last_finish - left[i])
        last_finish = right[i]
    time += right[i] - left[i]

if abs(last_finish - right[-1]) < abs(last_finish - left[-1]):
    time += abs(last_finish - right[-1])
    last_finish = left[-1]
else:
    time += abs(last_finish - left[-1])
    last_finish = right[-1]
time += right[-1] - left[-1]

print(time)
