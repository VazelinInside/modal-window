a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
num=[a, b, c, d, e]
num.sort(reverse=True)
kv=[]
for i in range(0, len(num)):
    kv.append(num[i]*num[i])
print(kv)