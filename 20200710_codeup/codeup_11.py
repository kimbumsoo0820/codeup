a =input()
count=len(a)-1
for i in a:
    print('['+i+('0'*count) +']')
    count-=1
