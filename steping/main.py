class Ans:
    def __init__(self, m: int, n: int):
        self.totalCost = 0
        self.allocated = [[0] * n for _ in range(m)]

class PathCost:
    def __init__(self):
        self.ind = [0, 0, 0, 0]
        self.cost = 0

pathCostVector = []



ans = Ans(3,2)
print(ans.allocated)