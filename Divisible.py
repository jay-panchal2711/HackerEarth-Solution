N = int(input())
data = list(input().split())

half = N/2
x = []
for i in range(N):
    if i < half:
        x.append(data[i][0])
    else:
        x.append(data[i][-1:])

temp = ''.join(x)

if (int(temp) % 10 == 0):
    print("Yes")
else:
    print("No")
