a,b,c = map(int,input().split())
check=a

for i in range(1,c):
    check*=b

print(check)
