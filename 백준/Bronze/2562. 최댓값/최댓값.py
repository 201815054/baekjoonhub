tmp =0
count = 0
for i in range(1,10):
    n = int(input())
    if n>tmp:
        tmp = n
        count = i
print(tmp)        
print(count)