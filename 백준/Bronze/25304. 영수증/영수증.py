x = int(input())
n = int(input())
cost_nums =[]
for i in range(n):
    c = list(map(int,input().split()))
    cost_nums.append(c)
tmp_sum = 0
for i in cost_nums:
    sum_ = i[0] * i[1]
    tmp_sum = tmp_sum+sum_
if tmp_sum == x:
    print("Yes")
else:
    print("No")