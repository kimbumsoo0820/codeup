a,b,c,d = map(int,input().split())
check=a

for i in range(1,d):
    check=check*b+c

print(check)
