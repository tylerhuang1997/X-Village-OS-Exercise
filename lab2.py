import multiprocessing
import random
import time
import numpy as np


def thread_func(a, b, matA, matB, result_queue):
    for row in range(a, b):
        result_queue.put( (row, np.matmul(matA[row], matB)) ) # Put a "tuple" into result_queue

def main():
    # x is the amount of row and colume
    x = 100

    # Generate two matrix A & B
    matA = np.random.randint(10, size = (x, x))
    matB = np.random.randint(10, size = (x, x))
    result_calc = np.zeros((matA.shape[0], matB.shape[1]))

    # Generate queue for communication
    result_queue = multiprocessing.Manager().Queue()
    processes = 10
    jobs = []
    start_time = time.time()

    for i in range(processes):
        process = multiprocessing.Process(target = thread_func, args = (i*(x//processes), (i+1)*(x//processes), matA, matB, result_queue))
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        result = result_queue.get()
        for i in result:
            result_calc[result[0]] = result[1]
    print(result_calc)

    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)
    print(np.matmul(matA, matB))
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result_calc))

if __name__ == "__main__":
    main()