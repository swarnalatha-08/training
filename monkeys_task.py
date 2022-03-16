def doorstate(monkey):
    count=0
    for door in range(1,101):
       if monkey % door == 0:
           count=count+1
    return count % 2
print("opened doors : ")
for monkey in range(1,101):
    ans = doorstate(monkey)
    if(ans == 1):
        print(monkey, end=" ")
print("\nclosed doors : ")
for monkey in range(1,101):
    ans = doorstate(monkey)
    if(ans == 0):
        print(monkey,end=' ')
