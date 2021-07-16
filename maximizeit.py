from itertools import product
k, m = map(int, input().split())
lst1 = []
for _ in range(k):
    x = list(map(int, input().split()))
    lst1.append(x)


for i in range(len(lst1)):
    lst1[i].pop(0)

lst = list(product(*lst1))

ans = []
for i in lst:
    summ = 0
    for j in i:
        summ += j**2
    ans.append(summ % m)
print(max(ans))
