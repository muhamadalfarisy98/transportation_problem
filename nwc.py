def north_west_corner(supply, demand):
    rows = len(supply)
    cols = len(demand)
    allocations = [[0 for _ in range(cols)] for _ in range(rows)]
    i, j = 0, 0

    while i < rows and j < cols:
        allocation = min(supply[i], demand[j])
        allocations[i][j] = allocation

        supply[i] -= allocation
        demand[j] -= allocation

        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1

    return allocations

def calculate_total_cost(cost_matrix, allocations):
    total_cost = 0
    rows = len(allocations)
    cols = len(allocations[0])

    for i in range(rows):
        for j in range(cols):
            total_cost += allocations[i][j] * cost_matrix[i][j]

    return total_cost

def main():
    cost_matrix = [[2, 3, 5, 1], [7, 3, 5, 1], [4, 1, 7, 2]]  
    supply = [8, 10, 20]  
    demand = [6, 8, 9, 15]  

    allocations = north_west_corner(supply, demand)

    print("\nHasil Alokasi:")
    for row in allocations:
        print(row)

    total_cost = calculate_total_cost(cost_matrix, allocations)
    print("Biaya Minimum nwc: ", total_cost)

if __name__ == "__main__":
    main()


