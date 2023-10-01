def greedy_algorithm(cost_matrix, supply, demand):
    num_suppliers = len(supply)
    num_consumers = len(demand)
    allocations = [[0] * num_consumers for _ in range(num_suppliers)]

    # Proses alokasi dengan algoritma Greedy
    while True:
        # Temukan sel dengan cost terendah
        min_cost = 10e3
        min_i, min_j = -1, -1

        for i in range(num_suppliers):
            for j in range(num_consumers):
                if cost_matrix[i][j] < min_cost and supply[i] > 0 and demand[j] > 0:
                    min_cost = cost_matrix[i][j]
                    min_i, min_j = i, j

        # Jika tidak ada sel yang dapat dialokasikan, keluar dari loop
        if min_i == -1:
            break

        # Alokasikan pengiriman sebanyak mungkin sesuai supply dan demand
        allocation = min(supply[min_i], demand[min_j])
        allocations[min_i][min_j] = allocation

        # Kurangi supply dan demand yang tersisa
        supply[min_i] -= allocation
        demand[min_j] -= allocation
    return allocations

def calculate_total_cost(cost_matrix, allocations):
    total_cost = 0
    rows, cols = len(allocations),len(allocations[0])

    for i in range(rows):
        for j in range(cols):
            total_cost += allocations[i][j] * cost_matrix[i][j]
    return total_cost

def main():
    cost_matrix = [[2, 3, 5, 1], [7, 3, 5, 1], [4, 1, 7, 2]] 
    supply = [8, 10, 20]  # supply
    demand = [6, 8, 9, 15]  # demand

    allocations = greedy_algorithm(cost_matrix, supply, demand)

    print("\nHasil Alokasi:")
    for row in allocations:
        print(row)

    total_cost = calculate_total_cost(cost_matrix, allocations)
    print("Biaya Minimum: ", total_cost)

if __name__ == "__main__":
    main()

# cost_matrix = [[2, 3, 5, 1], [7, 3, 5, 1], [4, 1, 7, 2]] 
#     supply = [8, 10, 20]  # supply
#     demand = [6, 8, 9, 15]  # demand

# cost_matrix = [[3,1,7,4], [2,6,5,9], [8,3,3,2]]  # table
    # supply = [300, 400, 500]  # supply
    # demand = [250, 350, 400, 200]  # demand

    # cost_matrix = [[19,30,50,10], [70,30,40,60], [40,8,70,20]]  # table
    # supply = [7,9,18]  # supply
    # demand = [5,8,7,14]  # demand
#