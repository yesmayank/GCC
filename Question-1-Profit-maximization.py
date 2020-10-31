case = list(map(int, input().split()))
predicted_days = case[0]
predicted_share = case[1:]
profit = []
for i, j in enumerate(predicted_share):
    pft = []
    for k,l in enumerate(predicted_share[i:]):
        pft.append(l-j)
    profit.append(max(pft))
p = max(profit)
if p >=0 :
    print(p)
else:
    print(0)
