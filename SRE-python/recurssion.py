def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#dynamic fibonacci
def dynamicfib(n):
    arr = [0] * (n+1)
    arr[0],arr[1] = 1,1
    for i in range(2,n+1,1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]
i = 0
def hanoitower(n, A, B, C):
    global i
    if n == 1:
        print(f"moved disk {n} from {A} to {B}")
        i+=1
        return
    hanoitower(n-1,A,C,B)
    print(f"moved disk {n} from {A} to {B}")
    i+=1
    hanoitower(n-1,C,B,A)

#hanoitower(15,'A','B','C')
weights = [2, 3, 4, 5, 9]
values = [3, 4, 8, 8, 10]
def knapsack_problem(weights, values, weight = 0, value = 0, i = 0, max_weight = 10):
    #recursive solution:
    if i == len(values):
        return value
    if weight + weights[i] < max_weight:
        added = knapsack_problem(weights, values, weight + weights[i], value+values[i], i+1)
        notadded = knapsack_problem(weights, values, weight, value, i + 1)
        return max(added, notadded)
    else:
        return value

# print(knapsack_problem(weights,values))
def dynamic_knapsack(weights, values,max_weights=10):
    n = len(weights)
    arr = [[0 for _ in range(max_weights + 1)] for _ in range(n + 1)]
    print(arr)

    for i in range(1,n+1):
        for j in range(max_weights+1):
            if weights[i-1] <= j:
                arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                arr[i][j] = arr[i-1][j]
    print(arr)
    print(arr[len(values)][max_weights]
)

def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]

def dictionary(string):
    dic = {"france" : "paris", "germany" : "berlin", "poland" : "warsaw"}
    print(dic["france"])

dictionary("a")


