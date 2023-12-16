dice = list(map(int, input().split()))

if len(set(dice)) == 1:
    # 같은 눈이 3개가 나오면
    reward = 10000 + dice[0] * 1000
elif len(set(dice)) == 2:
    # 같은 눈이 2개만 나오면
    for num in set(dice):
        if dice.count(num) == 2:
            reward = 1000 + num * 100
else:
    # 모두 다른 눈이 나오면
    reward = max(dice) * 100

print(reward)
