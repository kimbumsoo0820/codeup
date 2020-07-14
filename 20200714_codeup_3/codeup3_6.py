a = input()
a = int(a)
check = 1
result = 0
count = 0
while check <= a:
    result += check
    count += 1

    if (result >= a):
        break
    check += 1
print(result)
