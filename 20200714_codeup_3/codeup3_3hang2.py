a,b,c=map(int,input().split(' '))
check = a if a<b else b
print(check if check<c else c)