import logging as log
import numpy as np
from scipy.optimize import linear_sum_assignment

try:
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

    logger = log.getLogger('main')
    stream_handler = log.StreamHandler()
    formatter = log.Formatter('[%(levelname)s](%(filename)s:%(lineno)d)%(message)s')

    if __name__=='__main__':
        log.info('INFO 정보입니다')
        log.debug('DEBUG 정보입니다.')
        log.warning('WARNING 정보입니다.')
        log.error('ERROR 정보입니다.')
        log.critical('CRITICAL 정보입니다.')

except Exception as err:
    log.error(err)



