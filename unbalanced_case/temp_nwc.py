cost = [[2, 3, 5, 1], [7, 3, 5, 1], [4, 1, 7, 2]]  # table
supply = [8, 10, 20]  # supply
demand = [6, 8, 9, 15]  # demand


# cost = [[4, 8, 8], [16, 24, 16], [8,16,24]]  # table
# supply = [76,82,77]  # supply
# demand = [72,102,41]  # demand


startR = 0 # start row
startC = 0 # start col
ans = 0

# loop runs until it reaches the bottom right corner
while(startR != len(cost) and startC != len(cost[0])):
	# if demand is greater than supply
	if(supply[startR] <= demand[startC]):
		ans += supply[startR] * cost[startR][startC]
		# subtract the value of supply from the demand
		demand[startC] -= supply[startR]
		startR += 1
	# if supply is greater than demand
	else:
		ans += demand[startC] * cost[startR][startC]
		# subtract the value of demand from the supply
		supply[startR] -= demand[startC]
		startC += 1

print("The initial feasible basic solution is ", ans)


def isBalanced(supply,demand):
	return getTotalSupply(supply) == getTotalDemand(demand)

def getTotalSupply(supply):
	totalSupply = 0
	for val in supply : 
		totalSupply += val 
	return totalSupply

def getTotalDemand(demand):
	totalDemand = 0
	for val in demand : 
		totalDemand += val 
	return totalDemand

# if not isBalanced(supply, demand):
    #     if getTotalSupply(supply) < getTotalDemand(demand):
    #         # tambah baris dummy
    #         cost_matrix.append([0 for _ in range(len(cost_matrix[0]))])
    #         # tambah supply
    #         supply.append(getTotalDemand(demand) - getTotalSupply(supply))
    #     else :
    #         # tambah kolom dummy
    #         for i in range (len(cost_matrix)) :
    #             cost_matrix[i].append(0)
    #         # tambah demand
    #         demand.append(getTotalSupply(supply)- getTotalDemand(demand))


# #  versi OOP
# class TransportProblem:
#     def __init__(self, cost_matrix, supply, demand) -> None:
#         self.cost_matrix = cost_matrix
#         self.supply = supply 
#         self.demand = demand 

#     def north_west_corner(self):
#         rows = len(self.cost_matrix)
#         cols = len(self.cost_matrix[0])
#         allocations = [[0 for _ in range(cols)] for _ in range(rows)]
#         i, j = 0, 0
#         total_cost = 0

#         while i < rows and j < cols:
#             allocation = min(self.supply[i], self.demand[j])
#             allocations[i][j] = allocation

#             self.supply[i] -= allocation
#             self.demand[j] -= allocation
#             total_cost += allocations[i][j] * self.cost_matrix[i][j]

#             if self.supply[i] == 0:
#                 i += 1
#             if self.demand[j] == 0:
#                 j += 1

#         return allocations, total_cost

#     def calculate_total_cost(self, allocations):
#         total_cost = 0
#         rows = len(allocations)
#         cols = len(allocations[0])

#         for i in range(rows):
#             for j in range(cols):
#                 total_cost += allocations[i][j] * self.cost_matrix[i][j]

#         return total_cost

# def main():
#     cost_matrix = [[4, 8, 8], [16, 24, 16], [8,16,24]]  # table
#     supply = [76,82,77]  # supply
#     demand = [72,102,41]  # demand
#     tp = TransportProblem(cost_matrix, supply, demand)

#     allocations = tp.north_west_corner()

#     print("\nHasil Alokasi:")
#     for row in allocations:
#         print(row)

#     # total_cost = tp.calculate_total_cost(allocations)
#     # print(f"Biaya Minimum: {total_cost}")

# if __name__ == "__main__":
#     main()
