def solve_knapsack(profit, weight, capacity,n):
  K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

  for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i-1] <= w:
                K[i][w] = max(profit[i-1] + K[i-1][w-weight[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  return K[n][capacity]
 


profit = []
weight = []
print("enter size of profit/weight array")
n = int(input())
print("enter profit array")
for i in range(0, n):
    p = int(input())
    profit.append(p)
print("enter weight array")
for i in range(0, n):
    v = int(input())
    weight.append(v)
print("enter capacity")
capacity = int(input())
print("maximum profit = ",solve_knapsack(profit, weight, capacity,n))