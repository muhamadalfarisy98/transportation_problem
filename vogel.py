# findDiff - finds penalty
def findDiff(cost_matrix):
    rowDiff, colDiff = [], []
    for i in range(len(cost_matrix)):
        arr = cost_matrix[i][:]
        arr.sort()
        rowDiff.append(arr[1]-arr[0])

    col = 0
    while col < len(cost_matrix[0]):
        arr = []
        for i in range(len(cost_matrix)):
            arr.append(cost_matrix[i][col])
        arr.sort()
        col += 1
        colDiff.append(arr[1]-arr[0])

    return rowDiff, colDiff

# vogel_apprx - vogels aprx
def vogel_apprx(cost_matrix, supply, demand):
    rows,cols = len(supply),len(demand)
    allocations = [[0 for _ in range(cols)] for _ in range(rows)]
    ans = 0

    # loops sampai demand supply habis
    while max(supply) != 0 or max(demand) != 0:
        # finding the row and col difference
        row, col = findDiff(cost_matrix)

        # finding the maxiumum element in row difference array
        maxi1 = max(row)
        # finding the maxiumum element in col difference array
        maxi2 = max(col)

        # if the row diff max element is greater than or equal to col diff max element
        if(maxi1 >= maxi2):
            for ind, val in enumerate(row):
                if(val == maxi1):
                    # finding the minimum element in cost_matrix index where the maximum was found in the row difference
                    mini1 = min(cost_matrix[ind])
                    for ind2, val2 in enumerate(cost_matrix[ind]):
                        if(val2 == mini1):
                            # calculating the min of supply and demand in that row and col
                            mini2 = min(supply[ind], demand[ind2])
                            ans += mini2 * mini1
                            allocations[ind][ind2] = mini2
                            # subtracting the min from the supply and demand
                            supply[ind] -= mini2
                            demand[ind2] -= mini2
                            # if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                            if(demand[ind2] == 0):
                                for r in range(n):
                                    cost_matrix[r][ind2] = maxVal
                            # if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                            else:
                                cost_matrix[ind] = [maxVal for i in range(m)]
                            break
                    break

        # if the row diff max element is greater than col diff max element
        else:
            for ind, val in enumerate(col):
                if(val == maxi2):
                    # finding the minimum element in cost_matrix index where the maximum was found in the col difference
                    mini1 = maxVal
                    for j in range(n):
                        mini1 = min(mini1, cost_matrix[j][ind])

                    for ind2 in range(n):
                        val2 = cost_matrix[ind2][ind]
                        if val2 == mini1:
                            # calculating the min of supply and demand in that row and col
                            mini2 = min(supply[ind2], demand[ind])
                            ans += mini2 * mini1
                            allocations[ind2][ind] = mini2
                            # subtracting the min from the supply and demand
                            supply[ind2] -= mini2
                            demand[ind] -= mini2
                            # if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                            if(demand[ind] == 0):
                                for r in range(n):
                                    cost_matrix[r][ind] = maxVal
                            # if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                            else:
                                cost_matrix[ind2] = [maxVal for i in range(m)]
                            break
                    break

    return allocations, ans

#  test case
cost_matrix = [[2, 3, 5, 1], [7, 3, 5, 1], [4, 1, 7, 2]]
supply = [8, 10, 20]
demand = [6, 8, 9, 15]

maxVal = 10e3
n = len(cost_matrix)
m = len(cost_matrix[0])
ans = 0

allocations, total_cost = vogel_apprx(cost_matrix, supply, demand)
print("\nHasil Alokasi:")
for row in allocations:
    print(row)

print("\n")
print("Biaya Minimum vogel's approximation: ", total_cost)