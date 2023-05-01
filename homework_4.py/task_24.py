n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    temp = a[i] + a[(i-1) % n] + a[(i+1) % n] 
    # суммируем ягоды с текущего куста и двух соседних
    ans = max(ans, temp) 
    # обновляем максимальную сумму ягод

print(ans)