import logging as log
import numpy as np
from scipy.optimize import linear_sum_assignment

try:
    # 최소의 비용으로 모든 작업을 처리할 수 있는 기계와 작업의 조합을 찾는 문제는
    # Linear Sum Assignment Problem이고 Hungarian Algorithm을 이용해서 해결할 수 있다.
    # 그러므로 목적 함수 최소화를 위해 자주 사용되는 module인 scipy.optimize를
    # 사용하기에 적합하다. scipy.optimize의 linear_sum_assignment()라는 function은
    # Linear Sum Assignment Problem을 한 번에 풀어줄 수 있기에 현재 문제에
    # 적용할 수 있다.

    # 우선 linear_sum_assignment(array) function을 이용해서 optimal assignment를 찾아주는
    # find_optimal_assignment(array)라는 function을 하나 새로 만들었다.
    # 무작위로 만들어낸 n * n cost matrix를 parameter로 받아와서
    # optimal assignment에 해당하는 row 값과 column 값을 각각 row와 col에 할당하였다.
    # 그리고 최적화된 기계와 작업의 조합을 String으로 반환하기 위해서 result라는 변수를 하나 만들었다.
    # 이후에 for loop으로 column의 길이만큼 (n의 크기만큼) 기계 0부터 기계 n-1까지
    # 최적화된 작업 할당이 되어있는 col 안의 값을 순서대로 연결해서 result 변수에 concatenate해주고 마지막에
    # result를 반환해서 최적의 기계와 작업의 조합을 보여준다.
    def find_optimal_assignment(array):
        row, col = linear_sum_assignment(array)
        result = " "
        for i in range(len(col)):
            result += ("machine %d: job %d \n" % (i, col[i]))
        return result

    # 최적화된 기계와 작업 조합이 만들어내는 비용을 계산하기 위해서 find_total_cost(array, r, c)라는
    # function도 하나 만들었다. 이것도 똑같은 n * n cost matrix를 parameter로
    # 받아오지만, linear_sum_assignment(array)로 얻어진 row와 column의 값도 parameter로
    # 받아온다. 이 두 값들은 function이 실행되기 전에 생성되야 하고 위 function 안에서
    # 만들어진 row와 col 값들은 접근이 안 되기에 n * n cost matrix를 생성한 직후에
    # 한 번 더 직접 linear_sum_assignment(array)를 통해서 row와 column 값들을 새로 만들었다.
    # 그리고 array[row, column].sum()이라는 function을 통해 최적의 기계와 작업의 조합이
    # 만들어내는 비용을 하나씩 더해서 구할 수 있고 이 값을 토대로 String으로 반환하기 위해서
    # result라는 변수를 하나 새로 만들어서 total cost를 포함시켜서 반환했다.
    def find_total_cost(array, r, c):
        total_cost = array[r, c].sum()
        result = "The total cost is %d." % total_cost
        return result


    a = int(input("Enter a number: "))
    arr = np.random.randint(1,10, size=(a, a))
    print("data: \n", arr)

    row, col = linear_sum_assignment(arr)

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



