a = int(input())
b = input().split()
arr=[]
result=23
for i in range(0,a):
    arr.append(int(b[i]))
for i in range(0,a):
    if(arr[i]<result):
        result=arr[i]
print(result)