a=int(input())
check=1
result=0
while check<=a:
    if(check%2==0):
        result+=check
    check+=1
print(result)