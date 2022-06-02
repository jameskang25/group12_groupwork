import numpy as np
from scipy.optimize import linear_sum_assignment

def find_optimal_assignment(array):
    row, col = linear_sum_assignment(array)
    optimal_assignment = col
    result = " "
    for i in range(len(col)):
        result += ("machine %d: job %d \n" % (i, col[i]))
    return result

def find_total_cost(array, r, c):
    total_cost = array[r, c].sum()
    result = "The total cost is %d." % total_cost
    return result


a = int(input("Enter a number: "))
arr = np.random.randint(1,10, size=(a, a))
print("data: \n", arr)

print(find_optimal_assignment(arr))
print(find_total_cost(arr, row, col))



